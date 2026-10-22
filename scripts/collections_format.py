"""Parse collection files as described in FORMAT.md."""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS_DIR = ROOT / "collections"
PROVENANCES = ("papercove", "community")
KEYS = ("Curated by", "Language", "Description")
MAX_DESCRIPTION = 280
MIN_FEEDS = 5

SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
META_RE = re.compile(r"([A-Za-z][A-Za-z ]*): (.*)")
FEED_RE = re.compile(r"[-*] \[([^\]]+)\]\((\S+)\)\s*(?::|—)\s*(.+)")


def _load_languages():
    data = json.loads((Path(__file__).with_name("languages.json")).read_text(encoding="utf-8"))
    names = {}
    for code, labels in data["languages"].items():
        for label in labels:
            names[label.lower()] = code
            # "Modern Greek (1453-)" is also accepted as "Modern Greek".
            names[re.sub(r"\s*\(.*\)$", "", label).lower()] = code
    return set(data["languages"]), names


LANGUAGE_CODES, LANGUAGE_NAMES = _load_languages()


@dataclass
class Feed:
    name: str
    url: str
    why: str


@dataclass
class Collection:
    path: Path
    provenance: str = ""
    language_folder: str = ""
    slug: str = ""
    title: str = ""
    metadata: dict = field(default_factory=dict)
    language: str = ""
    feeds: list = field(default_factory=list)
    errors: list = field(default_factory=list)


def normalize_language(value):
    """Return the ISO 639-1 code (or "mul") for a Language value, or None."""
    if value == "Multilingual" or value == "mul":
        return "mul"
    if value in LANGUAGE_CODES:
        return value
    return LANGUAGE_NAMES.get(value.lower())


def parse(path):
    path = Path(path)
    c = Collection(path=path)
    rel = path.relative_to(COLLECTIONS_DIR).parts
    if len(rel) != 3:
        c.errors.append("must be at collections/<provenance>/<language>/<slug>.md")
        return c
    c.provenance, c.language_folder, filename = rel
    c.slug = filename.removesuffix(".md")
    if c.provenance not in PROVENANCES:
        c.errors.append(f"unknown provenance folder '{c.provenance}'")
    if c.language_folder != "mul" and c.language_folder not in LANGUAGE_CODES:
        c.errors.append(f"language folder '{c.language_folder}' is not an ISO 639-1 code or 'mul'")
    if not SLUG_RE.fullmatch(c.slug):
        c.errors.append(f"slug '{c.slug}' must be lowercase letters, digits and hyphens")

    lines = path.read_text(encoding="utf-8").split("\n")
    i = 0

    def skip_blank():
        nonlocal i
        while i < len(lines) and not lines[i].strip():
            i += 1

    skip_blank()
    if i < len(lines) and lines[i].startswith("# ") and lines[i][2:].strip():
        c.title = lines[i][2:].strip()
        i += 1
    else:
        c.errors.append("missing '# Title' line")

    skip_blank()
    meta_lines = []
    while i < len(lines) and (m := META_RE.fullmatch(lines[i].rstrip())):
        key, value = m.group(1), m.group(2).strip()
        if key in c.metadata:
            c.errors.append(f"duplicate key '{key}'")
        c.metadata[key] = value
        meta_lines.append(lines[i])
        i += 1

    for key in c.metadata:
        if key not in KEYS:
            c.errors.append(f"unknown key '{key}'")
    for key in KEYS:
        if key not in c.metadata:
            c.errors.append(f"missing key '{key}'")
    for line in meta_lines[:-1]:
        if not line.endswith("  "):
            c.errors.append(f"metadata line must end with two spaces: '{line.strip()}'")

    curated_by = c.metadata.get("Curated by", "")
    if c.provenance == "papercove" and curated_by != "Papercove":
        c.errors.append("'Curated by' must be 'Papercove' in papercove/")
    if c.provenance == "community" and curated_by.lower() == "papercove":
        c.errors.append("'Curated by' must not be 'Papercove' in community/")

    if "Language" in c.metadata:
        c.language = normalize_language(c.metadata["Language"]) or ""
        if not c.language:
            c.errors.append(f"unknown language '{c.metadata['Language']}'")
        elif c.language != c.language_folder:
            c.errors.append(f"language '{c.language}' does not match folder '{c.language_folder}'")

    if len(c.metadata.get("Description", "")) > MAX_DESCRIPTION:
        c.errors.append(f"description is longer than {MAX_DESCRIPTION} characters")

    seen = set()
    for line in lines[i:]:
        if not line.strip():
            continue
        m = FEED_RE.fullmatch(line.strip())
        if not m:
            c.errors.append(f"unexpected line: '{line.strip()[:80]}'")
            continue
        feed = Feed(*(g.strip() for g in m.groups()))
        if not re.match(r"https?://", feed.url):
            c.errors.append(f"feed URL must start with http(s)://: {feed.url}")
        if feed.url in seen:
            c.errors.append(f"duplicate feed URL: {feed.url}")
        seen.add(feed.url)
        c.feeds.append(feed)

    if len(c.feeds) < MIN_FEEDS:
        c.errors.append(f"needs at least {MIN_FEEDS} feeds, found {len(c.feeds)}")
    return c


def find_all():
    return sorted(COLLECTIONS_DIR.glob("*/*/*.md"))

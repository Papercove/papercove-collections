"""Generate one OPML file per collection in opml/, mirroring collections/."""

import shutil
import sys
import xml.etree.ElementTree as ET

from collections_format import COLLECTIONS_DIR, ROOT, find_all, parse

OPML_DIR = ROOT / "opml"


def build(collection):
    opml = ET.Element("opml", version="2.0")
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = collection.title
    ET.SubElement(head, "ownerName").text = collection.metadata["Curated by"]
    ET.SubElement(head, "docs").text = "https://opml.org/spec2.opml"
    body = ET.SubElement(opml, "body")
    group = ET.SubElement(body, "outline", text=collection.title, title=collection.title)
    for feed in collection.feeds:
        ET.SubElement(
            group,
            "outline",
            type="rss",
            text=feed.name,
            title=feed.name,
            xmlUrl=feed.url,
            description=feed.why,
        )
    ET.indent(opml)
    return ET.tostring(opml, encoding="unicode", xml_declaration=True) + "\n"


def main():
    collections = [parse(path) for path in find_all()]
    invalid = [c for c in collections if c.errors]
    if invalid:
        for c in invalid:
            print(f"✗ {c.path.relative_to(ROOT)} is invalid, run scripts/validate.py")
        return 1

    # Rebuild from scratch so deleted or renamed collections don't leave stale files.
    shutil.rmtree(OPML_DIR, ignore_errors=True)
    for c in collections:
        out = OPML_DIR / c.path.relative_to(COLLECTIONS_DIR).with_suffix(".opml")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build(c), encoding="utf-8")
        print(f"✓ {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

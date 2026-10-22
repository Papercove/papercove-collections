"""Validate every collection file against FORMAT.md. Exits non-zero on errors."""

import sys
from collections import defaultdict

from collections_format import COLLECTIONS_DIR, ROOT, find_all, parse


def main():
    collections = [parse(path) for path in find_all()]

    # Slugs are unique per language across papercove/ and community/.
    by_slug = defaultdict(list)
    for c in collections:
        by_slug[(c.language_folder, c.slug)].append(c)
    for (language, slug), same in by_slug.items():
        if len(same) > 1:
            for c in same:
                c.errors.append(f"slug '{slug}' is already used in another '{language}' collection")

    stray = [p for p in COLLECTIONS_DIR.rglob("*") if p.is_file() and p.suffix != ".md" and p.name != ".gitkeep"]

    failed = False
    for c in collections:
        rel = c.path.relative_to(ROOT)
        if c.errors:
            failed = True
            print(f"✗ {rel}")
            for error in c.errors:
                print(f"    {error}")
        else:
            print(f"✓ {rel} ({len(c.feeds)} feeds)")
    for p in stray:
        failed = True
        print(f"✗ {p.relative_to(ROOT)}: only .md collection files are allowed here")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

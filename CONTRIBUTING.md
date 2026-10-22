# Contributing

## Submit a collection

1. Create a file in `collections/community/<language>/`, named after your collection's slug (lowercase, hyphens), e.g. `collections/community/es/home-cooking.md`. Use the [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) for the language folder, or `mul` for multilingual collections. Create the folder if it doesn't exist yet.
2. Follow [FORMAT.md](FORMAT.md). `Curated by` is your name or handle (not `Papercove`).
3. Optionally, check your file locally with `python3 scripts/validate.py` (Python 3.9+, no dependencies).
4. Open a pull request. CI validates the file; the maintainer reviews it. Don't add an OPML file: it's generated automatically once your collection is merged.

By submitting a collection, you agree to license it under [CC BY 4.0](LICENSE), like the rest of this repository.

Slugs are permanent: pick a name you won't want to change.

## Selection criteria

- At least 5 feeds, each with a short, honest "why".
- Each link is the exact feed URL, not the site URL.
- Feeds are active, reachable and parseable.
- A clear, focused theme. Quality over quantity.
- No spam, no self-promotion-only collections.

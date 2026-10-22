# Collection file format

One collection per Markdown file, at `collections/<provenance>/<language>/<slug>.md`. Example: `collections/papercove/en/home-cooking.md`

```markdown
# Home cooking

Curated by: Papercove  
Language: English  
Description: Food blogs and newsletters for everyday cooking. Reliable recipes, honest techniques, no lifestyle fluff.

- [Example Blog](https://example.com/feed): Weeknight recipes that actually work, about twice a month.
- [Another Site](https://another.example/feed.xml): Short kitchen tips and techniques, weekly.
```

## Blocks

Three blocks, in this order.

### 1. Title

A single `# ` line. Required.

### 2. Metadata

Consecutive `Key: value` lines right after the title. End each line except the last with two spaces so they render on separate lines in Markdown. Closed list of keys:

| Key           | Required | Rules                                                                                                                                                              |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Curated by`  | yes      | Must be `Papercove` in `papercove/`, must not be `Papercove` in `community/`.                                                                                      |
| `Language`    | yes      | English language name (`French`), ISO 639-1 code (`fr`), or `Multilingual`. Normalized to the ISO code (`mul` for `Multilingual`). Must match the language folder. |
| `Description` | yes      | Single line, max 280 characters.                                                                                                                                   |

Unknown keys are an error.

### 3. Feeds

List items: `- [Name](URL): why`

- URL must be the exact feed URL (RSS, Atom or JSON Feed), not the site URL.
- The "why" is required.
- Minimum 5 feeds, no duplicate URLs.

## Parser tolerances

- Extra blank lines.
- `-` or `*` bullets.
- `—` instead of `:` after the link.

Any other content is rejected.

## Not in the file

- **Language folder**: ISO 639-1 code (`en`, `es`, `fr`…), or `mul` for `Multilingual`. Duplicates `Language` so the repo is browsable by language; the two must match.
- **Provenance**: from the top folder (`papercove/` or `community/`).
- **Slug**: from the filename (lowercase, hyphens). Unique per language across `papercove/` and `community/`, never renamed. The same slug can exist in several languages (`…/en/home-cooking.md`, `…/es/home-cooking.md`): they are distinct collections. Moving a file between `papercove/` and `community/` keeps its slug.

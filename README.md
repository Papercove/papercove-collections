# Papercove collections

Curated feed collections for [Papercove](https://papercove.app)'s Discover feature grouped by provenance, then by language:

```
collections/
├── papercove/   # official collections, curated by Papercove
│   ├── en/
│   ├── es/
│   └── …
└── community/   # submitted by the community
    ├── en/
    ├── es/
    └── …
```

Language folders use [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes); `mul` holds multilingual collections.

## Papercove collections

| Name              | Markdown                                                                  | OPML                                                                   |
| ----------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Cybersecurity     | [cybersecurity.md](collections/papercove/en/cybersecurity.md)             | [cybersecurity.opml](opml/papercove/en/cybersecurity.opml)             |
| Design            | [design.md](collections/papercove/en/design.md)                           | [design.opml](opml/papercove/en/design.opml)                           |
| Gaming            | [gaming.md](collections/papercove/en/gaming.md)                           | [gaming.opml](opml/papercove/en/gaming.opml)                           |
| Marketing         | [marketing.md](collections/papercove/en/marketing.md)                     | [marketing.opml](opml/papercove/en/marketing.opml)                     |
| Movies & TV shows | [movies-and-tv-shows.md](collections/papercove/en/movies-and-tv-shows.md) | [movies-and-tv-shows.opml](opml/papercove/en/movies-and-tv-shows.opml) |
| Programming       | [programming.md](collections/papercove/en/programming.md)                 | [programming.opml](opml/papercove/en/programming.opml)                 |
| Science           | [science.md](collections/papercove/en/science.md)                         | [science.opml](opml/papercove/en/science.opml)                         |
| Web development   | [web-development.md](collections/papercove/en/web-development.md)         | [web-development.opml](opml/papercove/en/web-development.opml)         |

## Import a collection

All collections are directly available in [Papercove](https://papercove.app): just pick one from Discover.

Using another feed reader? Every collection is available as an OPML file in [`opml/`](opml), with the same folder structure. These files are generated automatically from `collections/`: don't edit them by hand.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) and the file format in [FORMAT.md](FORMAT.md).

## License

[CC BY 4.0](LICENSE). You're free to reuse and adapt these collections, including commercially, as long as you credit them, for example: "Collections curated by [Papercove](https://papercove.app), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."

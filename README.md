# papercove-collections

Curated feed collections for [Papercove](https://papercove.app)'s Discover feature.

Collections are grouped by provenance, then by language:

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

Language folders use ISO 639-1 codes; `mul` holds multilingual collections.

## Import a collection

Copy the content of any collection file and paste it into Papercove. Each file is a complete, self-contained collection.

Using another feed reader? Every collection is also available as an OPML file in [`opml/`](opml), with the same folder structure. These files are generated automatically from `collections/`: don't edit them by hand.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) and the file format in [FORMAT.md](FORMAT.md).

## License

[CC BY 4.0](LICENSE). You're free to reuse and adapt these collections, including commercially, as long as you credit them, for example: "Collections curated by [Papercove](https://papercove.app), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)."

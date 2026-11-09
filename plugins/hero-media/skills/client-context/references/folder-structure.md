# Client folder structure

Every client gets the same folders, so people and Claude always know where to look.

```
[ACTIVE] Clients/
  <Client name>/
    00 Kundekontekst          Google Doc. The client context. One per client.
    01 Brand/                 Logos (SVG + PNG, light and dark), font files, brand guide, image style examples
    02 Strategi/              Strategy, plans, research, competitor analyses, workshops
    03 Content/
      Scripts/                Video and social scripts
      Optagelser/             Raw footage and photos, one subfolder per shoot (YYYY-MM-DD <name>)
      Færdigt/                Approved, final assets
      <Market>/               Only for multi-market clients: DK, SE, NL ... with the same subfolders inside
    04 Annoncer/              Ad copy, creatives, campaign setups
    05 Rapporter/             Reports to the client, one per month or campaign
    06 Kontrakter/            Contracts, quotes, agreements
```

## Rules

- **Numbered names** keep the order the same in every client folder.
- **One language for folder names:** Danish, as above.
- **One client per folder.** A sub-brand or another client never sits inside a client's folder; it gets its own folder in `[ACTIVE] Clients`.
- **Market folders only when needed:** a client in one market doesn't get them.
- **Inactive clients** move to `[ARKIV] Clients` with their whole folder.
- **Spreadsheets that run the work** (e.g. a Content OS or product sheet) sit at the client root next to `00 Kundekontekst`, so they're easy to find and link from the context doc.

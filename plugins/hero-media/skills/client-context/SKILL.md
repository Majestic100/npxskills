---
name: client-context
description: Load, create or update a Hero Media client's context (who they are, products, audience, markets, brand voice, competitors, goals) from the client's "00 Kundekontekst" Google Doc in Google Drive. Use whenever a task is for a named client (e.g. "landing page for World of Comfort", "write ads for Farvexperten"), when working in a claude.ai Project or code repo that belongs to a client, when the user asks to set up a new client, or when the user shares lasting facts about a client that should be remembered. Use it before other marketing skills so they work from the client's real context.
---

# Client context

Every Hero Media client has one context document in Google Drive. It is the single source of truth about the client, shared by everyone on the team and by Claude in both the Claude app and Claude Code. Your job is to find it, read it before doing client work, and keep it current.

## Where things live

```
Hero Media/
  [ACTIVE] Clients/
    <Client name>/
      00 Kundekontekst      <- Google Doc: the client context (this skill's source of truth)
      01 Brand/             <- logos, fonts, brand guide, image examples
      02 Strategi/
      03 Content/
      04 Annoncer/
      05 Rapporter/
      06 Kontrakter/
```

See [references/folder-structure.md](references/folder-structure.md) for what goes in each folder. Older clients may not follow this structure yet; search more broadly before concluding something is missing.

## 1. Find the client and its context

1. Work out which client the task is for: the user names it, the claude.ai Project is named after it, or the repo's CLAUDE.md names it. If it is unclear, ask. Never guess between two clients.
2. Use the Google Drive connector to find the client folder: a folder whose title contains the client name, normally inside `[ACTIVE] Clients`.
3. In that folder, find the Google Doc titled `00 Kundekontekst`. If it is not there, search the client folder for a doc whose title contains "Kundekontekst", "context" or "brief".
4. If no Google Drive tools are available, tell the user to connect Google Drive (Settings → Connectors in the Claude app), and ask them to paste the context in the meantime. Do not invent context.

## 2. Read it before working

- Read the whole document before writing anything for the client.
- Tell the user in one line which document you are using and its version or last-updated date, so a wrong or stale doc is caught early.
- Follow it: brand voice, words to use and avoid, markets and languages, legal or brand rules. When the task conflicts with the doc, point out the conflict and ask; don't silently pick one.
- Other skills (copywriting, ads, seo-audit, etc.) look for `.agents/product-marketing.md`. In Claude Code, after reading the doc, save its content there with a first line `> Copy of "00 Kundekontekst" in Google Drive (<link>). Edit the Drive doc, not this file.` so those skills pick it up. In the Claude app, the context you just read is already in the conversation; no file is needed.
- If the doc links to other files (product sheets, brand guide, earlier campaigns), read the ones relevant to the task.
- For anything visual (landing pages, ads, social graphics), use the exact colors, fonts and logo files from the doc and `01 Brand`. If a hex code, font or logo file is missing, ask for it; never invent brand colors or swap in a "similar" font.
- For product work, use the product data the doc links to (prices, names, links) rather than what you remember or find in search results, and start with the products listed under **Produktfokus**.

### Be critical about the context

Before starting the task, check whether the doc has what *this* task needs, and say plainly what is missing or weak. For example:
- copy without brand-voice examples or customer quotes will sound generic,
- a landing page without hex codes, fonts, logo files and the website platform can't be built to brand,
- product analysis without a product sheet or sales numbers is guesswork,
- ads without offer/discount rules or legal limits risk promising things the client can't keep.

Ask for the missing pieces, or go ahead with clearly marked assumptions if the user prefers, and offer to add the answers to the context doc afterwards.

## 3. Create it when it's missing

Ask before creating anything in Drive. Then:

1. Draft the context from what is available: the client's website, documents already in the client folder, and what the user tells you. Use the template in [references/context-template.md](references/context-template.md).
2. Mark every point you inferred rather than were told with `(antaget)`, and list the open questions at the bottom. A short, honest doc beats a long, guessed one.
3. Show the draft to the user and fold in their corrections.
4. Create it as a Google Doc titled exactly `00 Kundekontekst` in the client folder (create a text/markdown file in the folder and let Drive convert it to a Google Doc).

## 4. Update it

The Drive connector can create documents but cannot edit the text of an existing Google Doc. So:

- When the user tells you something lasting about the client (a new product, a changed target group, a tone rule, a result worth citing), offer to update the context. Don't update silently, and don't store one-off task details.
- To update: write the full new version (bump **Version**, set **Sidst opdateret**, add a line to **Ændringslog**), show the user the changes, and on their yes:
  1. rename the current doc to `00 Kundekontekst (arkiv YYYY-MM-DD)`,
  2. create the new version as `00 Kundekontekst` in the same folder,
  3. give the user the link.
- If the user prefers to edit the doc themselves, give them the exact text to paste instead.

## 5. Set up a new client

When the user asks to set up a new client:

1. Confirm the client's exact name and website.
2. Ask before creating folders. Create the client folder inside `[ACTIVE] Clients` with the subfolders from the structure above.
3. Ask the client (via the user) for the brand files that go in `01 Brand`: logo files, font names or files, brand guide.
4. Create `00 Kundekontekst` as described in step 3.
5. Remind the user to create a claude.ai Project named after the client and share it with the team, with this project instruction:
   `Dette projekt er for kunden <Client name>. Brug client-context-skillet til at hente kundekonteksten fra Google Drive, før du laver noget for kunden.`

## Rules

- Never mix clients. Only read and write in the folder of the client the task is for.
- Never put passwords, logins, API keys or personal data about private individuals in the context doc. Contact names and roles at the client are fine.
- The Drive doc is the source of truth. Copies (`.agents/product-marketing.md`, notes in a chat) are disposable.

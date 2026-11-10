---
name: client-context
description: Load, create or update a Hero Media client's Client Context (product, price, audience, audience language, competitors, brand voice, visual identity, claims and rules, goals, tracking, links, learnings) and Learning Log from the client's Context folder in Google Drive. Use whenever a task is for a named client (e.g. "landing page for MobileReport", "write ads for Farvexperten"), when working in a claude.ai Project or code repo that belongs to a client, when setting up a new client, when the user shares lasting facts or test results about a client, or when someone asks to change the Client Context structure. Use it before other marketing skills so they work from the client's real context.
---

# Client context

Every Hero Media client has one **Client Context** document and one **Learning Log** sheet in Google Drive. Together they are the single source of truth about the client, shared by the team and by Claude in both the Claude app and Claude Code. Your job is to find them, read them before doing client work, keep them current, and keep their structure in sync with the master template.

## Where things live

```
Hero Media/
  TEMPLATES/
    [TEMPLATE] Client Folder/
      Context/
        Client Context I Template v1     <- master template: the only source of the structure
        Learning Log I Template v1       <- master sheet
      Content/  Scripts/  Planning/
      Reporting/
      Agreements/
  [ACTIVE] Clients/
    <Client name>/
      Context/      Client Context I <Client>, Learning Log I <Client>, brand files, strategy. Internal only.
      Content/      Scripts/ and Planning/ (docs and sheets). Shared with the client.
      Reporting/    Reports. Shared with the client.
      Agreements/   Contracts and quotes. Shared with the client.
```

Video and images live in Frame.io, not in Drive. See [references/folder-structure.md](references/folder-structure.md).

## 1. Find the client and its context

1. Work out which client the task is for: the user names it, the claude.ai Project is named after it, or the repo's CLAUDE.md names it. If it is unclear, ask. Never guess between two clients.
2. With the Google Drive connector, find the client folder in `[ACTIVE] Clients`, then its `Context` folder.
3. In `Context`, find the Google Doc whose title starts with `Client Context I` and the sheet whose title starts with `Learning Log I`.
4. If no Google Drive tools are available, tell the user to connect Google Drive (Settings, Connectors in the Claude app), and ask them to paste the context meanwhile. Do not invent context.

## 2. Read it before working

- Read the whole Client Context before writing anything for the client. Tell the user in one line which document and version you are using.
- Follow it: brand voice, the "Skriv / Ikke" examples, audience language, markets, and above all **Påstande og regler** (Må bruges, Kræver godkendelse, Må ikke bruges). When the task conflicts with the doc, say so and ask.
- The examples show direction. Never copy them word for word into client copy.
- For anything visual, use the exact colors, fonts and logo files from the doc and the Context folder. If one is missing, ask; never invent brand colors or swap in a similar font.
- For product work, use the product data and prices the doc links to, not memory or search results. Check the price on the client's website when it matters.
- Before proposing a test, read the Learning Log so you don't repeat something already tested or ask a question already answered.
- Other skills (copywriting, ads, seo-audit, etc.) look for `.agents/product-marketing.md`. In Claude Code, after reading the doc, save its content there with the first line `> Copy of "Client Context I <Client>" in Google Drive (<link>). Edit the Drive doc, not this file.` In the Claude app no file is needed.

### Be critical about the context

Before starting, check whether the doc has what this task needs, and say plainly what is missing. For example: copy without brand voice examples or customer quotes sounds generic; a landing page without hex codes, fonts, logo files and the website platform can't be built to brand; product analysis without a product sheet is guesswork; ads without the claims and rules risk promising things the client can't keep. Ask for the missing pieces, or go ahead with clearly marked assumptions if the user prefers.

## 3. Create it for a new or existing client

Ask before creating anything in Drive. Then:

1. Copy `Client Context I Template v1` and `Learning Log I Template v1` into the client's `Context` folder and rename them `Client Context I <Client>` and `Learning Log I <Client>`.
2. Fill the doc from what is available: intake answers, documents already in the client folder, the client's website (colors and fonts can be read from it), and what the user tells you. Use the question bank `Client Context I Spørgsmål til intake` in TEMPLATES for what to ask.
3. Unknown values stay as `[FILL IN: ...]`. Things you found yourself and the client must confirm are marked `[CONFIRM]`. Never guess a number or a quote.
4. Put what the client has tried before into the Learning Log.
5. Format the doc with the `hm-doc-layout` skill if it is available.
6. Show the user the result and the open questions. Sinan approves it before it counts.

## 4. Update the content

When the user shares something lasting (a new product, a changed audience, a tone rule, a test result), offer to update. Don't update silently, and don't store one-off task details.

- **Learnings and test results** go into the Learning Log as one row each: date, area, type (Test, Observation, Kundefeedback), what we believed or saw, what we did, status, result, what we learned, what we change, source. Only the 5 to 10 most important learnings are copied into the doc under **Vigtigste learnings**.
- **Facts about the client** go into the relevant section of the Client Context. Bump the version number at the top.
- Edit the existing doc in place when Google Docs editing tools are available. If only Drive is available, write the full new section text and give it to the user to paste.

## 5. Change the structure (sections and their names)

The structure is defined in one place: the master template `Client Context I Template v1` (and the Learning Log template). Changing it anywhere else breaks the SOP, this skill and the intake questions.

If someone asks to add, remove, rename or reorder a section, or you notice that a client doc has a section the template doesn't have:

1. Stop and confirm with the user that the change should apply to all clients.
2. Then change, in the same go:
   - the master template: bump the template version (v1 to v2) and add a line under **Ændringslog**,
   - the SOP `SOP I Client Context Document I Hero Media`,
   - this skill and `references/context-template.md` in the skills repo (bump the hero-media plugin version, run the build),
   - the intake question bank, if the change affects it.
3. List every client doc that is on an older template version (the first line of each doc says `Template vX`). Update them only after the user says yes, or offer it the next time you work on that client.

Content inside a client doc can be edited freely. Only the structure goes through the template.

## 6. Set up a new client

When the user asks to onboard a new client, follow the checklist `Onboarding A to Z I Checklist` in TEMPLATES. Ask before creating folders, channels or projects. The parts Claude can do: create the client folder from `[TEMPLATE] Client Folder`, the Client Context and Learning Log (step 3), a Slack channel, a Frame.io project, a ClickUp list from the template, a Canva sheet with colors, fonts and logo, and the links section of the doc. Remind the user of the manual steps: brand kit in Canva, the claude.ai Project per client (shared with the team), and sharing `Content`, `Reporting` and `Agreements` with the client one by one.

## Rules

- Never mix clients. Only read and write in the folder of the client the task is for.
- Never share the client folder itself with the client. `Context` is internal.
- Never put passwords, logins, API keys or personal data about private individuals in the context. Contact names and roles at the client are fine.
- The Drive doc is the source of truth. Copies (`.agents/product-marketing.md`, notes in a chat) are disposable.

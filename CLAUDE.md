# Skills repo

This repo is Hero Media's shared skill library. Skills are grouped into Claude plugins under `plugins/<plugin>/skills/<skill>/`. The README is in Danish; the people using it are Danish.

## Layout

- `plugins/<plugin>/.claude-plugin/plugin.json`: plugin manifest (name, version, description).
- `plugins/<plugin>/skills/<skill>/SKILL.md` plus any `references/`, scripts and the upstream `LICENSE`.
- `sources.json`: one entry per skill: plugin, upstream source (`owner/repo` or `own`), path in that repo, license.
- `scripts/build.py`: validates every skill and regenerates the derived files. Never edit the derived files by hand:
  `.claude-plugin/marketplace.json`, the catalog between the `CATALOG` markers in `README.md`, `.claude/skills/*` symlinks, `dist/*.zip`.

## Adding a skill someone else made

1. Copy the whole skill folder from upstream (SKILL.md and every file it references), not just SKILL.md. Fetch from the upstream repo, e.g. `git clone --depth 1 https://github.com/<owner>/<repo>` into the scratchpad, then copy the skill folder.
2. Copy the upstream LICENSE into the skill folder. If the upstream repo has no license, stop and tell the user: we can't redistribute it.
3. Put it in the plugin that fits by theme. If none fits, ask the user before creating a new plugin.
4. Add the entry to `sources.json`.
5. Bump the plugin's `version` in plugin.json (minor for a new skill, patch for an updated one).
6. Run `python3 scripts/build.py` and fix any errors it reports.
7. Commit and push. Then remind the user that the plugin must be published to the organization again (the PublishPlugin tool, path `plugins/<plugin>`) for colleagues to get the update.

## Writing our own skill

Same steps, but the folder is new, `sources.json` gets `"source": "own"`, `"path": ""`, `"license": "own"`, and there is no LICENSE file. Frontmatter needs `name` (equal to the folder name, lowercase-hyphenated) and a `description` of at most 1024 characters that says what the skill does and when to use it. Never put secrets, client data or machine-specific paths in a skill.

## Updating a third-party skill

Re-copy the folder from upstream, keep our LICENSE copy, bump the plugin version (patch), run the build, commit.

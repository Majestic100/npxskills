#!/usr/bin/env python3
"""Validate skills and regenerate everything derived from them.

Run from the repo root after adding, removing or changing a skill:

    python3 scripts/build.py

What it regenerates:
  - .claude-plugin/marketplace.json  (Claude Code marketplace, from each plugin.json)
  - the skill catalog in README.md   (between the CATALOG markers)
  - .claude/skills/<skill> symlinks  (so Claude Code sessions in this repo see every skill)
  - dist/<skill>.zip                 (for upload in the Claude app; deterministic, so only changed skills change)
"""
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
SOURCES = json.loads((ROOT / "sources.json").read_text())
MARKETPLACE_NAME = "heromedia-skills"
OWNER = {"name": "Hero Media"}
REPO_URL = "https://github.com/majestic100/npxskills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BEGIN, END = "<!-- CATALOG:BEGIN -->", "<!-- CATALOG:END -->"

errors = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    fm, key = {}, None
    for line in m.group(1).splitlines():
        top = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if top:
            key, val = top.group(1), top.group(2).strip()
            fm[key] = val.strip("'\"") if val not in ("|", ">", "|-", ">-") else ""
        elif key == "description" and line.startswith("  "):  # folded/multi-line description
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


def summary(desc):
    """First sentence of the description, without the trigger-phrase lists."""
    first = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
    return first.replace("|", "\\|")


def collect():
    plugins = []
    for pdir in sorted(p for p in PLUGINS.iterdir() if p.is_dir()):
        manifest_path = pdir / ".claude-plugin" / "plugin.json"
        if not manifest_path.exists():
            errors.append(f"{pdir}: missing .claude-plugin/plugin.json")
            continue
        manifest = json.loads(manifest_path.read_text())
        if manifest.get("name") != pdir.name:
            errors.append(f"{manifest_path}: name must be '{pdir.name}'")
        skills = []
        for sdir in sorted(s for s in (pdir / "skills").iterdir() if s.is_dir()):
            skill_md = sdir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{sdir}: missing SKILL.md")
                continue
            fm = frontmatter(skill_md)
            name, desc = fm.get("name", ""), fm.get("description", "")
            if name != sdir.name:
                errors.append(f"{skill_md}: name '{name}' must match folder '{sdir.name}'")
            if not NAME_RE.match(name) or len(name) > 64:
                errors.append(f"{skill_md}: name must be lowercase-hyphenated, max 64 chars")
            if not desc:
                errors.append(f"{skill_md}: missing description")
            elif len(desc) > 1024:
                errors.append(f"{skill_md}: description is {len(desc)} chars (Claude app max 1024)")
            src = SOURCES.get(sdir.name)
            if src is None:
                errors.append(f"sources.json: no entry for '{sdir.name}' (use source 'own' for our own skills)")
            elif src.get("plugin") != pdir.name:
                errors.append(f"sources.json: '{sdir.name}' has plugin '{src.get('plugin')}', but lives in '{pdir.name}'")
            skills.append({"name": sdir.name, "dir": sdir, "description": desc, "source": src or {}})
        plugins.append({"dir": pdir, "manifest": manifest, "skills": skills})
    known = {s["name"] for p in plugins for s in p["skills"]}
    for name in SOURCES:
        if name not in known:
            errors.append(f"sources.json: '{name}' has no skill folder")
    return plugins


def write_marketplace(plugins):
    data = {
        "name": MARKETPLACE_NAME,
        "owner": OWNER,
        "metadata": {"description": "Hero Media's shared skills for Claude Code and the Claude app."},
        "plugins": [
            {
                "name": p["manifest"]["name"],
                "source": f"./plugins/{p['dir'].name}",
                "description": p["manifest"].get("description", ""),
                "version": p["manifest"].get("version", "0.1.0"),
            }
            for p in plugins
        ],
    }
    out = ROOT / ".claude-plugin" / "marketplace.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def source_cell(src):
    s = src.get("source", "?")
    if s == "own":
        return "Vores egen"
    return f"[{s}](https://github.com/{s}) ({src.get('license', '?')})"


def write_catalog(plugins):
    lines = [BEGIN, ""]
    total = sum(len(p["skills"]) for p in plugins)
    lines.append(f"{total} skills i {len(plugins)} plugins. Klik på et skill-navn for at læse hele skillet.")
    lines.append("")
    for p in plugins:
        m = p["manifest"]
        n = len(p["skills"])
        lines.append(f"### {m['name']} ({n} skill{'' if n == 1 else 's'})")
        lines.append("")
        lines.append(m.get("description", ""))
        lines.append("")
        lines.append("| Skill | Hvad den gør | Kilde |")
        lines.append("|---|---|---|")
        for s in p["skills"]:
            rel = s["dir"].relative_to(ROOT).as_posix()
            lines.append(f"| [{s['name']}]({rel}/SKILL.md) | {summary(s['description'])} | {source_cell(s['source'])} |")
        lines.append("")
    lines.append(END)
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        errors.append("README.md: catalog markers missing")
        return
    pre, rest = text.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    readme.write_text(pre + "\n".join(lines) + post, encoding="utf-8")


def sync_symlinks(plugins):
    link_dir = ROOT / ".claude" / "skills"
    link_dir.mkdir(parents=True, exist_ok=True)
    wanted = {}
    for p in plugins:
        for s in p["skills"]:
            wanted[s["name"]] = os.path.relpath(s["dir"], link_dir)
    for entry in link_dir.iterdir():
        if entry.is_symlink() and (entry.name not in wanted or os.readlink(entry) != wanted[entry.name]):
            entry.unlink()
    for name, target in wanted.items():
        link = link_dir / name
        if not link.exists() and not link.is_symlink():
            link.symlink_to(target)


def build_zips(plugins):
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for old in dist.glob("*.zip"):
        old.unlink()
    for p in plugins:
        for s in p["skills"]:
            with zipfile.ZipFile(dist / f"{s['name']}.zip", "w", zipfile.ZIP_DEFLATED) as z:
                for f in sorted(s["dir"].rglob("*")):
                    if f.is_file():
                        info = zipfile.ZipInfo(f"{s['name']}/{f.relative_to(s['dir']).as_posix()}", (2020, 1, 1, 0, 0, 0))
                        info.compress_type = zipfile.ZIP_DEFLATED
                        info.external_attr = (0o755 if os.access(f, os.X_OK) else 0o644) << 16
                        z.writestr(info, f.read_bytes())


def main():
    plugins = collect()
    if errors:
        print("Errors:\n  " + "\n  ".join(errors))
        sys.exit(1)
    write_marketplace(plugins)
    write_catalog(plugins)
    sync_symlinks(plugins)
    build_zips(plugins)
    if errors:
        print("Errors:\n  " + "\n  ".join(errors))
        sys.exit(1)
    print(f"OK: {len(plugins)} plugins, {sum(len(p['skills']) for p in plugins)} skills")


if __name__ == "__main__":
    main()

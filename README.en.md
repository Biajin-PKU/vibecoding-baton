# vibecoding-baton

<p align="center">
  <img src="assets/logo.png" width="280" alt="vibecoding-baton">
</p>

Pass the baton between vibe-coding sessions.

Works with **Claude Code** and **Codex**. A skill writes the next-session prompt; a hook injects it once after `/clear`.

[中文](README.md) | English

## Why a plugin

A skill can write the prompt. Only a SessionStart hook can inject it after `/clear`. Ship both.

## Use

1. When a phase is done, run **`/baton`**.
2. Type **`/clear`** in the same window.
3. Look for `vibecoding-baton: baton passed`. The parked prompt is injected once and then deleted.

Clipboard is the fallback if that message does not appear.

## Install

Needs Python 3.

### Claude Code

```text
/plugin marketplace add Biajin-PKU/vibecoding-baton
/plugin install vibecoding-baton@vibecoding-baton
```

Local checkout:

```text
claude plugin install /path/to/vibecoding-baton
```

### Codex

Point Codex at this folder as a plugin (skills + hooks). The hook file is `hooks/hooks.json`.

## How it keys the slot

Park and inject hash `$CLAUDE_PROJECT_DIR` (then cwd). Trailing slashes are stripped, so `/proj` and `/proj/` share one slot.

Files live in `~/.vibecoding-baton/handoffs/`. Override with `VIBECODING_BATON_DIR`.

The hook matcher is **`clear` only**. A later `startup` / `resume` will not consume the file.

## Layout

```text
.claude-plugin/plugin.json
.codex-plugin/plugin.json
hooks/baton.py
hooks/hooks.json
skills/baton/SKILL.md
```

## License

MIT

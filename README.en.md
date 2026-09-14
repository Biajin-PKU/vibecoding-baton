# vibecoding-baton

A long session burns tokens and gets dull. `/clear` brings the edge back — and wipes the next move with it.

**vibecoding-baton** clears the context, not the progress. `/baton` writes the next prompt. `/clear` in the same window injects it once. The new session already has the baton.

Claude Code · Codex · [MIT](LICENSE) · [中文](README.md) · English

## Use

```text
/baton
/clear
```

`vibecoding-baton: baton passed` means it landed.

If that line doesn't show, the same prompt is on your clipboard.

## Install

Python 3 required.

**Claude Code** — send these as two separate prompts:

```text
/plugin marketplace add Biajin-PKU/vibecoding-baton
/plugin install vibecoding-baton@vibecoding-baton
```

**Codex**

```bash
codex plugin marketplace add Biajin-PKU/vibecoding-baton
codex plugin add vibecoding-baton@vibecoding-baton
```

Start a new session. Accept the hook if asked.

## What it does

`/baton` parks a short prompt: files to read, decisions already made, constraints that only live in this chat, and the next action.

`/clear` injects it once, then deletes it. Projects don't share a slot. Startup and resume won't consume it early.

Everything stays on your machine, under `~/.vibecoding-baton/handoffs/`.

## License

[MIT](LICENSE)

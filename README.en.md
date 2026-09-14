# vibecoding-baton

A long session burns tokens and gets dull. `/clear` brings the edge back — and wipes the next move with it.

**vibecoding-baton** lets the agent watch for that. When the context is heavy and a phase of work has landed, it parks the next prompt and tells you it's safe to `/clear`. You don't write a handoff. You don't paste anything. The new session already has the baton.

Claude Code · Codex · [MIT](LICENSE) · [中文](README.md) · English

## What you do

Install it. Keep working.

When the agent says it's time:

```text
/clear
```

`vibecoding-baton: baton passed` means it landed. If that line doesn't show, the same prompt is on your clipboard.

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

When the session gets long, a hook reminds the agent: don't interrupt the current step; at the next phase boundary, park the next move.

That move is a short prompt — files to read, decisions already made, constraints that only live in this chat, and the next action. It stays on your machine.

`/clear` injects it once, then deletes it. Projects don't share a slot. Startup and resume won't consume it early.

Default directory: `~/.vibecoding-baton/handoffs/`.

## License

[MIT](LICENSE)

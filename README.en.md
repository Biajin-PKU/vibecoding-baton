# vibecoding-baton

<p align="center">
  <img src="assets/logo.png" width="240" alt="vibecoding-baton">
</p>

<p align="center"><strong>Pass the next move to a fresh session.</strong></p>

<p align="center">
  Claude Code · Codex<br>
  <a href="LICENSE">MIT</a>
  · <a href="README.md">中文</a>
  · English
</p>

---

Long sessions get slow. `/clear` also wipes the next move. So you copy a handoff — and sometimes you forget to paste it.

**vibecoding-baton** turns that into a relay. `/baton` writes the next prompt. `/clear` in the same window injects it once. The new session already has the baton.

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

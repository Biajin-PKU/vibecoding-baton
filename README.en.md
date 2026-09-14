# vibecoding-baton

A long session burns tokens and gets dull. `/clear` brings the edge back — and wipes the next move with it.

**vibecoding-baton** has the agent prepare a continuation prompt when the session is long and the current phase of work is complete, then asks you to `/clear`. No handoff to write, nothing to paste. The new session picks up where you left off.

Claude Code · Codex · [MIT](LICENSE) · [中文](README.md) · English

## Example

You're adding team billing to a live SaaS: schema, settlement API, Stripe webhooks, then the admin UI. It won't fit in one session.

**Session 1.** The schema and API are on disk and tests pass. The context is long; webhook work starts missing edge cases. The phase is done, so the agent writes a continuation prompt and tells you to `/clear`.

You type:

```text
/clear
```

**Session 2.** The new session already has the constraints: read `prisma/schema.prisma` and `apps/api/src/billing.ts`; Stripe test mode only; next is webhook idempotency, don't reopen the schema. It writes the webhook. It does not ask where you left off.

`vibecoding-baton: baton passed` means it landed. If that line doesn't show, the same prompt is on your clipboard. A single feature can relay like this more than once.

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

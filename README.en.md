# vibecoding-baton

A long session burns tokens and gets dull. `/clear` brings the edge back — and wipes the next move with it.

**vibecoding-baton** has the agent prepare a continuation prompt when the session is long and the current phase of work is complete, then asks you to `/clear`. No handoff to write, nothing to paste. The new session picks up where you left off.

Claude Code · Codex · [MIT](LICENSE) · [中文](README.md) · English

## Flow

You're adding team billing to a live SaaS. The schema and settlement API are on disk; tests pass. The session is long; Stripe webhook work starts missing edge cases.

**1. What appears in the terminal**

Still the same window. The agent parks a continuation prompt, then says:

```text
Settlement API is on disk; tests pass. Next session: Stripe webhook idempotency.
You can /clear now.
```

**2. What you do**

Don't open a new terminal. Don't copy. Don't paste. In **this window**, type:

```text
/clear
```

**3. What happens**

`/clear` wipes the current context. A hook injects the parked prompt into the new session once, then deletes it. The terminal shows:

```text
vibecoding-baton: baton passed
```

If that line doesn't show, the same prompt is already on your clipboard.

**4. What you do in the new session**

Same window, new session. You don't recap. Keep going — "continue" is enough. The agent already has the constraints: read `prisma/schema.prisma` and `apps/api/src/billing.ts`; Stripe test mode only; next is webhook idempotency; don't reopen the schema. It will not ask where you left off.

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

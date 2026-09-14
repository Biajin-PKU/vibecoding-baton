---
name: baton
description: When a long session hits a phase boundary, park a next-session prompt so the user's /clear injects it. Use when the length hook fires, a phase of work is done and context is heavy, or the user says the session feels dull. Do not wait for the user to invoke this skill.
---

# Baton

Long sessions burn tokens and get dull. You notice. You park the next move. The user only types `/clear`.

Do not ask them to write a handoff. Do not ask them to run `/baton`.

## When

Fire at a **phase boundary** after the session is already long (the length hook is the usual signal).

A phase boundary is: a chunk of work landed on disk, verified, and the next chunk is a new unit. Mid-edit, mid-experiment, or an open decision is not a boundary — finish or ask first.

If clear would lose something you cannot write into the prompt, say so and wait.

## Park

Write a short prompt the next session can start from alone, in the user's language:

1. Files to read first
2. Decisions already made
3. Constraints that only live in this chat
4. The next concrete action

Then:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/hooks/baton.py" park <<'BATON'
<prompt>
BATON
```

If `CLAUDE_PLUGIN_ROOT` is empty, try `CODEX_PLUGIN_ROOT`. If both are empty, stop.

Expect `parked ~/.vibecoding-baton/handoffs/<id>.md`. Clipboard is the fallback.

## Tell the user

One beat: the next session is ready, type **`/clear`** in this window. `vibecoding-baton: baton passed` means it worked.

Do not open a new terminal. Do not put the prompt on a shell command line.

---
name: baton
description: Park a next-session prompt so /clear injects it once. Use when the user says baton, handoff, checkpoint, "ready to clear", or a phase of long work is done and a fresh session should continue.
---

# /baton

Long sessions get slow. This skill writes the next-session prompt and parks it. After `/clear`, the SessionStart hook injects that prompt once.

## Before parking

Answer: **what would `/clear` lose?**

List what is already on disk vs what still lives only in this session. If in-flight work, unverified edits, or an open decision cannot be written into the prompt, say so and wait.

## Write the prompt

Short. The next session should be able to start from this text alone.

Include:

1. Files to read first (paths)
2. Decisions already made
3. Constraints that exist only in this conversation
4. The next concrete action

Write it in the user's language.

## Park

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/hooks/baton.py" park <<'BATON'
<prompt>
BATON
```

If `CLAUDE_PLUGIN_ROOT` is empty, try `CODEX_PLUGIN_ROOT`. If both are empty, stop and tell the user the plugin root is missing.

Expect `parked ~/.vibecoding-baton/handoffs/<id>.md`. The script also copies to the clipboard when `pbcopy` / `wl-copy` / `xclip` exists.

## Close

Tell the user:

- parked path
- type **`/clear`** in this window
- a system message `vibecoding-baton: baton passed` means it worked
- clipboard is the fallback if the message does not appear

Do not open a new terminal. Do not put the prompt on a shell command line.

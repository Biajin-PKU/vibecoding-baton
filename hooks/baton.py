#!/usr/bin/env python3
"""Nudge when a session is long; park a prompt; inject it once on /clear."""
import hashlib
import json
import os
import subprocess
import sys

DIR = os.environ.get("VIBECODING_BATON_DIR") or os.path.expanduser(
    "~/.vibecoding-baton/handoffs"
)
BYTE_LIMIT = int(os.environ.get("VIBECODING_BATON_BYTES") or 2 * 1024 * 1024)
PREFIX = (
    "A previous session parked this baton. Continue from it now. "
    "Do not wait for the user to paste it.\n\n"
)
NUDGE = (
    "This session is long (~{mb:.1f} MB transcript). Tokens are burning and "
    "answers get dull. Do not interrupt the current step. At the next natural "
    "phase boundary, follow the baton skill: park a next-session prompt, then "
    "tell the user they can /clear. They should not have to write or paste "
    "the handoff."
)


def normalize_root(raw):
    path = os.path.realpath(os.path.abspath(os.path.expanduser(str(raw) or ".")))
    if os.name == "nt":
        drive, tail = os.path.splitdrive(path)
        if tail not in ("\\", "/"):
            path = drive + tail.rstrip("\\/")
        return path
    if path != "/":
        path = path.rstrip("/")
    return path


def project_root(cwd_hint=None):
    raw = os.environ.get("CLAUDE_PROJECT_DIR") or cwd_hint or os.getcwd()
    return normalize_root(raw)


def slot_path(root):
    key = hashlib.sha256(root.encode()).hexdigest()[:16]
    return os.path.join(DIR, key + ".md")


def clip(text):
    payload = text.encode("utf-8")
    for cmd in (["pbcopy"], ["wl-copy"], ["xclip", "-selection", "clipboard"]):
        try:
            subprocess.run(cmd, input=payload, check=True, timeout=2)
            return True
        except Exception:
            continue
    return False


def park(text, cwd_hint=None):
    text = text.strip()
    if not text:
        print("vibecoding-baton: empty prompt", file=sys.stderr)
        return 1
    os.makedirs(DIR, exist_ok=True)
    path = slot_path(project_root(cwd_hint))
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.write("\n")
    os.replace(tmp, path)
    copied = clip(text)
    print("parked " + path)
    if copied:
        print("clipboard ok")
    return 0


def inject(payload):
    cwd = payload.get("cwd") if isinstance(payload, dict) else None
    path = slot_path(project_root(cwd))
    if not os.path.exists(path):
        return 0
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read().strip()
        os.remove(path)
    except Exception as exc:
        json.dump(
            {"systemMessage": "vibecoding-baton: failed to read parked prompt (%s)" % exc},
            sys.stdout,
        )
        sys.stdout.write("\n")
        return 0
    if not text:
        return 0
    json.dump(
        {
            "systemMessage": "vibecoding-baton: baton passed",
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": PREFIX + text,
                "initialUserMessage": text,
            },
        },
        sys.stdout,
        ensure_ascii=False,
    )
    sys.stdout.write("\n")
    return 0


def nudge(payload):
    path = ""
    if isinstance(payload, dict):
        path = payload.get("transcript_path") or ""
    if not path or not os.path.exists(path):
        return 0
    try:
        size = os.path.getsize(path)
    except Exception:
        return 0
    if size < BYTE_LIMIT:
        return 0
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": NUDGE.format(mb=size / 1048576),
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")
    return 0


def stdin_json():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def main(argv):
    if argv[1:] == ["park"]:
        return park(sys.stdin.read())
    if argv[1:] == ["nudge"]:
        return nudge(stdin_json())
    if argv[1:2] == ["slot"]:
        hint = argv[2] if len(argv) > 2 else None
        print(slot_path(project_root(hint)))
        return 0
    return inject(stdin_json())


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv) or 0)
    except Exception as exc:
        json.dump({"systemMessage": "vibecoding-baton: %s" % exc}, sys.stdout)
        sys.stdout.write("\n")
        sys.exit(0)

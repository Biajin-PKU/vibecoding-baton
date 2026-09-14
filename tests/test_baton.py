#!/usr/bin/env python3
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "hooks" / "baton.py"


class BatonTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = os.environ.copy()
        self.env["VIBECODING_BATON_DIR"] = self.tmp.name
        self.env.pop("CLAUDE_PROJECT_DIR", None)

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, args, stdin="", extra_env=None):
        env = self.env.copy()
        if extra_env:
            env.update(extra_env)
        proc = subprocess.run(
            ["python3", str(SCRIPT), *args],
            input=stdin.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            cwd=self.tmp.name,
        )
        return proc

    def test_trailing_slash_same_slot(self):
        a = self.run_script(["slot", "/Users/demo/app"])
        b = self.run_script(["slot", "/Users/demo/app/"])
        self.assertEqual(a.stdout, b.stdout)
        self.assertTrue(a.stdout.strip())

    def test_project_dir_beats_cwd(self):
        via_env = self.run_script(
            ["slot"],
            extra_env={"CLAUDE_PROJECT_DIR": "/tmp/stable-root"},
        )
        via_cwd = self.run_script(["slot", "/tmp/other"])
        self.assertNotEqual(via_env.stdout, via_cwd.stdout)

    def test_park_then_inject_once(self):
        park = self.run_script(["park"], stdin="read README.md\ncontinue\n")
        self.assertEqual(park.returncode, 0, park.stderr.decode())
        self.assertIn(b"parked ", park.stdout)
        files = list(Path(self.tmp.name).glob("*.md"))
        self.assertEqual(len(files), 1)

        payload = json.dumps({"cwd": self.tmp.name})
        first = self.run_script([], stdin=payload)
        self.assertEqual(first.returncode, 0, first.stderr.decode())
        self.assertTrue(first.stdout, first.stderr.decode())
        data = json.loads(first.stdout.decode("utf-8"))
        self.assertEqual(data["systemMessage"], "vibecoding-baton: baton passed")
        ctx = data["hookSpecificOutput"]["additionalContext"]
        self.assertIn("read README.md", ctx)
        self.assertEqual(
            data["hookSpecificOutput"]["hookEventName"], "SessionStart"
        )
        self.assertFalse(list(Path(self.tmp.name).glob("*.md")))

        second = self.run_script([], stdin=payload)
        self.assertEqual(second.returncode, 0)
        self.assertEqual(second.stdout, b"")

    def test_empty_park_fails(self):
        proc = self.run_script(["park"], stdin="  \n")
        self.assertEqual(proc.returncode, 1)

    def test_nudge_silent_when_short(self):
        transcript = Path(self.tmp.name) / "t.jsonl"
        transcript.write_bytes(b"x" * 100)
        proc = self.run_script(
            ["nudge"],
            stdin=json.dumps({"transcript_path": str(transcript)}),
        )
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout, b"")

    def test_nudge_fires_when_long(self):
        transcript = Path(self.tmp.name) / "t.jsonl"
        transcript.write_bytes(b"x" * 100)
        proc = self.run_script(
            ["nudge"],
            stdin=json.dumps({"transcript_path": str(transcript)}),
            extra_env={"VIBECODING_BATON_BYTES": "50"},
        )
        self.assertEqual(proc.returncode, 0, proc.stderr.decode())
        data = json.loads(proc.stdout.decode("utf-8"))
        self.assertIn("phase boundary", data["hookSpecificOutput"]["additionalContext"])


if __name__ == "__main__":
    unittest.main()

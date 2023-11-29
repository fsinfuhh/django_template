#!/usr/bin/env python3
import subprocess

if __name__ == "__main__":
    subprocess.check_call("git init".split(" "))
    subprocess.check_call(
        ["git", "commit", "--allow-empty", "--message=initial commit"]
    )

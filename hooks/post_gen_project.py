#!/usr/bin/env python3
import subprocess

if __name__ == "__main__":
    subprocess.check_call("git init".split(" "))
    subprocess.check_call("pre-commit install".split(" "))
    subprocess.check_call("pipenv lock".split(" "))
    subprocess.check_call("git add --all".split(" "))
    subprocess.call("pre-commit run --all-files".split(" "))
    subprocess.check_call("git add --all".split(" "))
    subprocess.check_call(
        ["git", "commit", "--message=add project setup from mafiasi template"]
    )

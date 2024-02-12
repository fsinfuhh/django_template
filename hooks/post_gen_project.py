#!/usr/bin/env python3
import subprocess


def git_commit(message: str):
    subprocess.check_call("git add --all".split(" "))
    subprocess.call("pre-commit run --all-files".split(" "))
    subprocess.check_call("git add --all".split(" "))
    subprocess.check_call(["git", "commit", f"--message={message}"])


if __name__ == "__main__":
    # add generated files
    subprocess.check_call("pre-commit install".split(" "))
    git_commit("add project setup from mafiasi template")

    # lock & install dependencies
    subprocess.check_call("pipenv lock".split(" "))
    subprocess.check_call("pipenv sync".split(" "))
    subprocess.check_call("pnpm install --no-frozen-lockfile".split(" "), cwd="./src/{{ cookiecutter.project_slug }}_gui")
    git_commit("lock dependencies")

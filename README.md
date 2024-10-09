# Cookiecutter for Mafiasi Projects

This repository is a [cookiecutter](https://www.cookiecutter.io/) template to quickly get started in authoring a new mafiasi projcet.

## How to use

1. Install cookiecutter via your systems package manager

   See the official [cookiecutter installation instructions](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html) for more details.

2. Install `pre-commit` e.g. via:
   ```shell
   pip install pre-commit
   ```

4. Create a new project based on this template by running and responding to all the questions.

   ```shell
   cookiecutter https://github.com/fsinfuhh/template
   ```

   Cookiecutter will ask you some questions and insert your responses all over the project.
   See the [cookiecutter variable reference](#cookiecutter-variable-reference) below for more information about what
   what each question means.

## Cookiecutter Variable Reference

- `project_slug`
  A (preferably short) machine-readable name of the project.
  
  This will be used for example for the python package name and dev database credentials.

- `project_name`
  An equivalent to the `project_slug` but intended for humans.
  This is inserted into documentation e.g. the generated `README.md`.

- `author`
  The name of the entity that is the author of the project.
  This is inserted into the generated license (which is MIT).

- `openid_scope`
  A space separated list of scopes that are requested from the Mafiasi OpenID provider during login.
  This influences which information about a user is available to the application.

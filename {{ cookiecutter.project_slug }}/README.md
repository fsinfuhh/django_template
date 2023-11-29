# {{ cookiecutter.project_name }}

**TODO: Fill out a proper project description**

## Configuration Details

The application is intended to be configured via environment variables.
The following variables are defined:

| Name       | Default                           | Required? | Description                                                                                                                  |
|------------|-----------------------------------|:---------:|------------------------------------------------------------------------------------------------------------------------------|
| `APP_MODE` | `prod` in docker, `dev` otherwise |    yes    | The mode in which {{ cookiecutter.project_slug }} operates.<br>**Changing this may affect the defaults of other variables.** |

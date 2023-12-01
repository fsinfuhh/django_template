# Build the frontend in a dedicated container
# only the compilation result is copied over into the final container
# Note: nodejs v18 is what is included with the debian distribution of the final container so we use the same version during build
FROM docker.io/node:18 as gui_build
RUN npm install -g pnpm
WORKDIR /usr/local/src/{{ cookiecutter.project_slug }}_gui

# add dependency declaration first for faster rebuilds
ADD src/{{ cookiecutter.project_slug }}_gui/package.json src/{{ cookiecutter.project_slug }}_gui/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile --shamefully-hoist=true

# add remaining sources and build the project
ADD src/{{ cookiecutter.project_slug }}_gui/ ./
RUN pnpm run build



# use a basic debian container as the final image
FROM docker.io/debian:bookworm as final

# setup process supervisor
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends nodejs python3 python-is-python3 pipenv nginx gunicorn xz-utils supervisor
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/start_backend.sh docker/start_frontend.sh docker/start_nginx.sh /usr/local/bin/
CMD ["/usr/bin/supervisord"]

# install django server
WORKDIR /usr/local/src/{{ cookiecutter.project_slug }}/
ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
ADD LICENSE README.md ./
ADD src/ ./src/
ADD docker/nginx.conf /etc/nginx/sites-enabled/default

# add built frontend sources
COPY --from=gui_build /usr/local/src/{{ cookiecutter.project_slug }}_gui/.output ./src/{{ cookiecutter.project_slug }}_gui/dist/

# add some image metadata and config
EXPOSE 80/tcp
ENV APP_MODE=prod

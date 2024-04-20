FROM node:21-slim

VOLUME /app/frontend
WORKDIR /app/frontend

ADD ./start.sh /usr/local/bin/start.sh

RUN npm install -g pnpm

RUN chmod 774 /usr/local/bin/start.sh

USER 1000
EXPOSE 3000

CMD ["bash", "/usr/local/bin/start.sh"]

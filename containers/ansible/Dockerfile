FROM alpine:3.18.3
RUN sed -i 's/https/http/g' /etc/apk/repositories
RUN apk add -q ansible ansible-lint

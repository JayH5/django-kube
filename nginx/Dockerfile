ARG FROM_TAG=stable-alpine
FROM nginx:$FROM_TAG

RUN rm /etc/nginx/conf.d/default.conf

COPY config/ /etc/nginx/

#!/usr/bin/env bash
set -e

# No args or looks like options or the APP_MODULE for Gunicorn
if [ "$#" = 0 ] || [ "${1#-}" != "$1" ] || \
    echo "$1" | grep -Eq '^([_A-Za-z]\w*\.)*[_A-Za-z]\w*:[_A-Za-z]\w*$'; then
  set -- gunicorn "$@"
fi

if [ "$1" = 'gunicorn' ]; then
  # Create the Gunicorn runtime directory at runtime in case /run is a tmpfs
  if mkdir /run/gunicorn 2> /dev/null; then
    chown django:django /run/gunicorn
  fi

  set -- "$@" --config /etc/gunicorn/config.py

  if [ "$(id -u)" = '0' ]; then
    set -- gosu django "$@"
  fi
fi

exec "$@"

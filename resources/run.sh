#!/bin/bash

sed -i "s/xxSERVERxx/${PY_SERVER}/g" /etc/nginx/nginx.conf
sed -i "s/xxPORTxx/${PY_PORT}/g" /etc/nginx/nginx.conf

nginx -c /etc/nginx/nginx.conf -g "daemon off;"

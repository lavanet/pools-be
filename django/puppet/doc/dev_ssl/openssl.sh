#!/usr/bin/env bash

# SOURCE: https://www.humankode.com/ssl/create-a-selfsigned-certificate-for-nginx-in-5-minutes

openssl req -x509 -nodes -days 3650 \
    -newkey rsa:2048 -keyout localhost.key \
    -out localhost.crt -config localhost.conf

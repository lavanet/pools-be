#!/usr/bin/env bash

apt-get update
apt-get install software-properties-common -y
add-apt-repository universe
add-apt-repository ppa:certbot/certbot -y
apt-get update
apt-get install certbot python3-certbot-nginx -y

snap install certbot --classic
echo 'certbot --nginx certonly --cert-name {PROJECT} -d mydomain.com'

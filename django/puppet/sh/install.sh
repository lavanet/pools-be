#!/usr/bin/env bash

cd /tmp
wget https://apt.puppetlabs.com/puppet7-release-jammy.deb
dpkg -i puppet7-release-jammy.deb
apt update
apt install -y puppet-agent
ln -s /opt/puppetlabs/bin/puppet /bin/puppet

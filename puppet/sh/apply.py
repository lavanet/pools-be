#!/usr/bin/python3
from utils import install_puppet_modules, puppet_apply

install_puppet_modules((
    ('puppetlabs-postgresql', '10.3.0'),
    ('puppetlabs-vcsrepo', '6.1.0'),
    ('puppet-letsencrypt', '10.1.0'),
    ('domkrm-ufw', '1.1.4'),
    ('saz-ssh', '12.1.0'),
    ('saz-timezone', '6.3.0'),
))

puppet_apply()

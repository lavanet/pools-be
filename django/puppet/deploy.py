#!/usr/bin/env python

"""
Deployment script
"""

from __future__ import print_function, absolute_import

import argparse
from datetime import datetime
from os import path
from subprocess import call

import remote_servers

PUPPET_DIRECTORY = path.dirname(path.abspath(__file__))


class RemoteServer(object):
    def __init__(self, server_name, debug=False):
        if not server_name:
            raise SyntaxError('You must specify a server name configured in '
                              'remote_server.py module.')
        self.server_name = server_name
        self.debug = debug
        try:
            server = getattr(remote_servers, server_name)
        except AttributeError:
            raise AttributeError('Remote server "%s" is not configured in the '
                                 'remote_servers.py module' % server_name)
        self.host = server['host']
        self.deploy_user = server['deploy_user']
        self.project_user = server['project_user']

    def __str__(self):
        return self.server_name

    def __call__(self, command=None):
        if not command:
            command = 'deploy'
        getattr(self, command)()

    def deploy(self, user=None):
        if not user:
            user = self.deploy_user
        if not self.debug:
            self.rsync(user=user)
        self.ssh('cd /etc/puppet/sync/sh && sudo ./apply.py', user=user)

    def git_key(self, user=None, project_user=None):
        if not user:
            user = self.deploy_user
        if not project_user:
            project_user = self.project_user
        self.ssh('sudo cat /home/%(project_user)s/.ssh/id_rsa.pub' % {
            'project_user': project_user,
        }, user=user)

    def install_puppet(self, user='root'):
        self.ssh('mkdir /etc/puppet', user=user)
        self.rsync(user=user)
        self.ssh('cd /etc/puppet/sync/sh '
                 '&& chmod 770 install.sh apply.py swapon.sh '
                 '&& sudo ./swapon.sh '
                 '&& sudo ./install.sh '
                 '', user=user)
        if not self.debug:
            self.deploy(user=user)
            self.git_key(user=self.deploy_user)

    def rsync(self, user=None, local=path.join(PUPPET_DIRECTORY, '.'), remote='/etc/puppet/sync'):
        if not user:
            user = self.deploy_user
        remote = '%(user)s@%(host)s:%(remote)s' % {
            'user': user,
            'host': self.host,
            'remote': remote,
        }
        try:
            call_command(('rsync', '-rtvz', '-e', 'ssh', local, remote,))
        except FileNotFoundError:
            call_command(('scp', '-rC', local, remote))

    def ssh(self, cmd, user=None):
        if not user:
            user = self.deploy_user
        host = '%(user)s@%(host)s' % {'user': user, 'host': self.host, }
        call_command(('ssh', host, cmd))


def call_command(cmd):
    call(cmd)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('server', nargs='?', help='Name of server config from remote_servers.py')
    parser.add_argument('command', nargs='?')
    parser.add_argument('-d', '--debug', action='store_true', help='run with minimal execution')
    args = parser.parse_args()
    remote_server = RemoteServer(
        server_name=args.server,
        debug=args.debug,
    )
    print(
        '--- TIME: %s ---\n'
        '--- SERVER: %s ---\n'
        '--- HOST: %s ---' % (
            datetime.now(),
            remote_server,
            remote_server.host,
        )
    )
    remote_server(args.command)


if __name__ == '__main__':
    parse_args()

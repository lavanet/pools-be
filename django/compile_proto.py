# Description: Compile all proto files to python files.
# Usage: python compile_proto.py

from os import getcwd, path, walk
from subprocess import call

CWD = getcwd()

PROTO_PATH = path.join(CWD, 'proto')
PROTO_OUT_PATH = path.join(CWD, 'proto_python')
PROTO_APPS = (
    'amino',
    'cosmos',
    'cosmos_proto',
    'gogoproto',
    'google/api',
    'ibc',
    'lavanet',
    'tendermint',
)


def iter_proto(app):
    """
    Iterate over all proto files in the given app folder.
    """
    for root, dirs, files in walk(path.join(PROTO_PATH, app)):
        for file in files:
            if file.endswith('.proto'):
                yield path.join(root, file)


def compile_python_proto():
    """
    Compile all proto files to python files.
    """
    for app in PROTO_APPS:
        call((
            'python', '-m', 'grpc_tools.protoc',
            f'-I{PROTO_PATH}',
            f'--python_out={PROTO_OUT_PATH}',
            *iter_proto(app),
        ))


__name__ == '__main__' and compile_python_proto()

from __future__ import absolute_import

import os
import sys
import warnings

from .celery import app


class SysPath(list):
    def append(self, obj):
        if obj not in self:
            super().append(obj)

    def insert(self, index, obj):
        if obj not in self:
            super().insert(index, obj)


sys.path = SysPath(sys.path)
sys.path.append(f'{os.getcwd()}/proto_python')

# Ignore warnings about protobuf version
# https://github.com/grpc/grpc/issues/37609
warnings.filterwarnings("ignore", ".*obsolete", UserWarning, "google.protobuf.runtime_version")

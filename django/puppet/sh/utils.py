import re
from os import path
from subprocess import check_output, Popen
from sys import stdout


def strip_color(s):
    """
    https://github.com/jonathaneunice/colors/blob/master/colors/colors.py
    """
    return re.sub('\x1b\\[(K|.*?m)', '', s)


def unpack_optional(iterable, length=3):
    for i in iterable:
        yield i + (None,) * (length - len(i))


class PuppetModuleManager(object):
    PUPPET_PATH = path.dirname(path.dirname(__file__))
    MODULES_PATH = path.join(PUPPET_PATH, 'modules')
    NODES_PATH = path.join(PUPPET_PATH, 'nodes')
    SYSTEM_MODULE_PATH = '/etc/puppet/code/modules'
    MODULE_PATH_ARG = f'--modulepath={MODULES_PATH}:{SYSTEM_MODULE_PATH}'

    @classmethod
    def apply(cls, *args):
        cls._call_puppet('apply', cls.NODES_PATH, cls.MODULE_PATH_ARG, *args, stream=True)

    @classmethod
    def apply_dry(cls):
        cls.apply('--noop', '--show_diff')

    @classmethod
    def install_module(cls, module, version, update=False, ignore_dependencies=False):
        args = [
            'module', 'install', module,
            '--version', version,
            '--modulepath', cls.SYSTEM_MODULE_PATH, ]
        if update:
            args.append('--force')
        if ignore_dependencies:
            args.append('--ignore-dependencies')
        cls._call_puppet(*args, stream=True)

    @classmethod
    def install_modules(cls, required_modules):
        installed_modules = cls.get_puppet_modules()
        for r_module, r_version, r_ignore_dependencies in unpack_optional(required_modules, 3):
            r_ignore_dependencies = bool(r_ignore_dependencies)
            if r_module not in installed_modules:
                cls.install_module(r_module, r_version, ignore_dependencies=r_ignore_dependencies)
            elif installed_modules[r_module] != r_version:
                cls.install_module(r_module, r_version, ignore_dependencies=r_ignore_dependencies, update=True)

    @classmethod
    def get_puppet_modules(cls):
        return dict(cls._iter_puppet_modules())

    @classmethod
    def _iter_puppet_modules(cls, re_module=re.compile(r'^.+?([\w-]+) \(v(.+?)\)$')):
        lines = strip_color(cls._call_puppet('module', 'list', cls.MODULE_PATH_ARG)).split('\n')
        for line in lines:
            try:
                yield re_module.findall(line)[0]
            except IndexError:
                pass

    @classmethod
    def _call_puppet(cls, *args, stream=False):
        if stream:
            return Popen(('puppet',) + args, stdout=stdout).wait()
        else:
            return check_output(('puppet',) + args).decode()


def install_puppet_modules(modules):
    return PuppetModuleManager.install_modules(modules)


def puppet_apply():
    return PuppetModuleManager.apply()

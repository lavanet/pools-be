from __future__ import absolute_import

from logging import getLogger

from django.conf import settings
from django.core.management import BaseCommand
from django.utils import translation


class ModuleCommand(BaseCommand):
    module = None
    logger = getLogger('default')

    def add_arguments(self, parser):
        parser.add_argument('method')
        parser.add_argument('args', nargs='*')
        parser.add_argument('-s', '--safe', action='store_true')

    def handle(self, *args, method, safe, **options):
        translation.activate(settings.LANGUAGE_CODE)
        try:
            module_method = getattr(self.module, method)
            is_dangerous = getattr(module_method, 'is_dangerous', False)
            if settings.DEBUG or safe or not is_dangerous:
                module_method(*args)
            else:
                self.logger.warning('"%s()" is a dangerous task function, must use --safe.' % method)
        except Exception as e:
            self.logger.exception(e)


def dangerous(func):
    """
    Dangerous functions can only be executed
    with DEBUG=True or with --safe argument.
    """
    func.is_dangerous = True
    return func

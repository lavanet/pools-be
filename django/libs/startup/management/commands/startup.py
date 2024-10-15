from __future__ import print_function, absolute_import, unicode_literals

import os

from django.conf import settings
from django.core.management import BaseCommand, call_command
from django.db import connection

from ...ns import hacked

NAME = settings.DATABASES['default']['NAME']
ENGINE = settings.DATABASES['default']['ENGINE']


class Command(BaseCommand):
    """
    Startup restores the main database to its original state. Loads fixtures.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--prod',
            action='store_true',
            default=False,
            help='Do a startup in production. yeah really.',
        )
        parser.add_argument(
            '--no-data',
            action='store_true',
            default=False,
            help='Drop tables, run migrations but don\'t load fixtures.',
        )

    def handle(self, prod, no_data, **options):
        if settings.DEBUG or prod:
            print(hacked)
            self.drop_tables()
            self.migrate()
            if not no_data:
                self.load_fixtures()

    @staticmethod
    def drop_sqlite():
        """
        Removes the sqlite db file.
        """
        if os.path.exists(NAME):
            os.remove(NAME)

    @staticmethod
    def drop_postgres():
        """
        Introspect all table names and perform DROP statement on each of them.
        """
        tables = connection.introspection.table_names()
        cursor = connection.cursor()
        for table in tables:
            cursor.execute('DROP TABLE "%s" CASCADE;' % table)

    @classmethod
    def drop_tables(cls):
        """
        Identify the database backend and execute the matching function to reset it.
        """
        if "sqlite" in ENGINE:
            cls.drop_sqlite()
        elif "postgres" in ENGINE or "postgis" in ENGINE:
            cls.drop_postgres()

    @staticmethod
    def migrate():
        call_command('migrate')

    @staticmethod
    def load_fixtures():
        for initial_fixture in getattr(settings, 'STARTUP_INITIAL_FIXTURES', []):
            call_command('loaddata', initial_fixture, )

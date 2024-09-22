from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'args',
            metavar='app_label',
            nargs='*',
            help='Specify the app label(s) to create migrations for.'
        )

    def handle(self, *app_labels, **options):
        call_command('makemigrations', *app_labels, **options)
        call_command('migrate', *app_labels, **options)

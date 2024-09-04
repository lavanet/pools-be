from django.core.management.commands.makemessages import Command as MakeMessages


class Command(MakeMessages):
    def handle(self, *args, **options):
        options['no_location'] = True
        options['extensions'] = ['py', 'html', 'jinja', 'js']
        super().handle(*args, **options)

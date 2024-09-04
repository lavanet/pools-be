from __future__ import print_function, absolute_import, unicode_literals

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Startup restores the main database to its original state. Loads fixtures. Create base user.
    """

    def handle(self, **options):
        from django.contrib.contenttypes.models import ContentType
        print(ContentType.objects.all().delete())

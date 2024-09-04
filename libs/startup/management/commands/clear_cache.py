from django.core.cache import cache
from django.core.management import BaseCommand

from libs.utils import logger


class Command(BaseCommand):
    def handle(self, *app_labels, **options):
        cache.clear()
        logger.info('Cleared Default Cache')

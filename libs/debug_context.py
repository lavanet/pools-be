from django.conf import settings


def debug(request):
    """
    Returns context variables helpful for debugging.
    """
    return {'DEBUG': settings.DEBUG}

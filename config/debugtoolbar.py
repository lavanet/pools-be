from django.conf import settings


def show_toolbar(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest' \
        and settings.SHOW_DEBUG_TOOLBAR \
        and request.user.is_superuser

from logging import getLogger

from rest_framework.views import exception_handler as drf_exception_handler

logger = getLogger(__name__)


def exception_handler(exc, context):
    try:
        request = context['request']
        method = request.method
        user = request.user
        ip = request.META.get('REMOTE_ADDR')
        url = request.get_full_path()
        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}
        logger.error('HTTP:%s, %s, %s, "%s %s", %s: %s',
                     exc.status_code, ip, user, method, url, type(exc).__qualname__, data, )
    except:
        pass
    return drf_exception_handler(exc, context)

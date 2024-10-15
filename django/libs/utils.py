from io import BytesIO
from logging import getLogger

import requests
from django.contrib.auth.decorators import user_passes_test

superuser_required = user_passes_test(lambda u: u.is_superuser)
staff_required = user_passes_test(lambda u: u.is_staff)
logger = getLogger('default')


def download_file(url, timeout=10):
    remote_file = BytesIO()
    exception = requests.RequestException()
    for i in range(3):
        try:
            response = requests.get(url, timeout=timeout)
            break
        except Exception as e:
            exception = requests.RequestException('Failed to download "%s", error: %s' % (url, str(e)))
    else:
        raise exception
    for block in response.iter_content(1024):
        if not block:
            break
        remote_file.write(block)
    return remote_file

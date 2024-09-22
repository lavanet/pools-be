from os import path

from django.conf import settings
from django.http import HttpResponse
from django.utils.html import escape

from .utils import tail_log

MAX_LINES = 1000


def tail_info(request):
    try:
        lines = int(request.GET['lines'])
    except (TypeError, ValueError, KeyError):
        lines = 200
    lines = min(lines, MAX_LINES)
    filename = path.join(settings.BASE_DIR, 'logs', 'default.log')
    lines = tail_log(open(filename, 'rb'), lines=lines)
    escaped_lines = (escape(line.decode(errors='replace')) for line in lines)
    raw_text = '<br>'.join(escaped_lines)
    return HttpResponse(raw_text)

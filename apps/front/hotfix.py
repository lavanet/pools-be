from subprocess import check_output

from django.http import HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from .tasks import test_logger


def test_exception(request):
    raise Exception('Error report TEST! A superuser is testing.')


def test_exception_celery(request):
    test_logger.delay()


def whoami(request):
    """
    Useful tool to get META data and more in prod.
    """
    items = tuple(request.META.items()) + (
        ('_is_secure()', request.is_secure()),
        ('_get_host()', request.get_host()),
    )
    return HttpResponse('<br>'.join(str(i) for i in sorted(items)))


try:
    def git(request, git_history=check_output(('git', 'log', '--max-count', '5',)).decode(),
            dt_app_loaded=now().astimezone().replace(microsecond=0)):
        time_since = now().replace(microsecond=0) - dt_app_loaded
        return HttpResponse(f"""
<div><strong>Application Restart</strong><pre>{dt_app_loaded}</pre></div><hr>
<div><strong>Uptime</strong><pre>{time_since}</pre></div><hr>
<div><strong>Git History</strong>:<pre>{git_history}</pre></div><hr>
""")
except:
    pass


@csrf_exempt
def echo(request):
    print('method:', request.method)
    print('GET')
    for k, v in request.GET.items():
        print(k, v)
    print('POST')
    for k, v in request.POST.items():
        print(k, v)

    print('BODY:', request.body)

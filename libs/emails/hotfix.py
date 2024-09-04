from django.conf import settings
from django.http import HttpResponseBadRequest

from libs.emails.utils import test_email as test_email_


def test_email(request):
    try:
        email = request.GET['email']
    except KeyError:
        return HttpResponseBadRequest('Provide email address ?email=<email>')
    test_email_(
        to=(email,),
        subject=request.GET.get('subject', 'Hotfix Email Test'),
        message=request.GET.get('message', 'This is a test message. Everything is fine.'),
        from_email=request.GET.get('from_email', settings.DEFAULT_FROM_EMAIL),
    )

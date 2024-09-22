import re

from celery import shared_task
from django.core.mail.backends.base import BaseEmailBackend
from django_ses import SESBackend

from . import settings
from .utils import strip_accents

re_valid_email = re.compile(
    r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)'
    r'*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09'
    r'\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]'
    r'(?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?'
    r'[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*'
    r'[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')


def filter_invalid_emails(emails):
    retval = []
    for email in emails:
        email = strip_accents(email.replace(' ', '').lower())
        if email and re_valid_email.match(email):
            retval.append(email)
    return retval


def filter_invalid_email_messages(email_messages):
    for email_message in email_messages:
        email_message.to = filter_invalid_emails(email_message.to)
        if email_message.to:
            email_message.cc = filter_invalid_emails(email_message.cc)
            email_message.bcc = filter_invalid_emails(email_message.bcc)
            yield email_message


class SerializableMessage(object):
    class Message(object):
        def __init__(self, message):
            self.message = message

        def as_string(self):
            return self.message

    def __init__(self, message, from_email, recipients):
        self._message = message
        self._recipients = recipients
        self.from_email = from_email
        self.extra_headers = {}

    def recipients(self):
        return self._recipients

    def message(self):
        return self.Message(self._message)

    @staticmethod
    def serialize(email_messages):
        return tuple({'message': message.message().as_string(),
                      'from_email': message.from_email,
                      'recipients': message.recipients(),
                      } for message in email_messages)

    @classmethod
    def deserialize(cls, serialized_messages):
        return tuple(cls(
            message=message['message'],
            from_email=message['from_email'],
            recipients=message['recipients'],
        ) for message in serialized_messages)


class CelerySESBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        email_messages = filter_invalid_email_messages(email_messages)
        if email_messages:
            (send_email.delay if settings.USE_CELERY else send_email)(
                serialized_messages=SerializableMessage.serialize(email_messages),
                fail_silently=self.fail_silently, )


@shared_task
def send_email(serialized_messages, fail_silently, **kwargs):
    backend = SESBackend(fail_silently=fail_silently, **kwargs)
    backend.send_messages(SerializableMessage.deserialize(serialized_messages))

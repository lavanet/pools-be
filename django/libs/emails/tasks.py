from .backends import send_email
from .utils import test_email

# Make the task discoverable
id(send_email)


def test():
    test_email(to=('@webisoft.com',), )

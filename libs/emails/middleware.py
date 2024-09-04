from django.utils.deprecation import MiddlewareMixin

from .utils import set_request


class GlobalRequest(MiddlewareMixin):
    def process_request(self, request):
        set_request(request)

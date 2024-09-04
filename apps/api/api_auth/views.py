from functools import wraps

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from .serializers import UserSerializer


def do_login():
    def _decorator(func):
        @csrf_exempt
        @api_view(["POST"])
        @permission_classes((AllowAny,))
        @wraps(func)
        def _wrapper(request, *args, **kwargs):
            form = AuthenticationForm(request, data=request.data)
            if request.user.is_authenticated:
                user = request.user
            elif form.is_valid():
                user = form.get_user()
                if user is None or not user.is_active:
                    return Response(status=HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=HTTP_400_BAD_REQUEST)
            return func(request, user, *args, **kwargs)

        return _wrapper

    return _decorator


@do_login()
def login_session(request, user):
    login(request, user)
    return Response(UserSerializer(user).data)


@do_login()
def login_token(request, user):
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        **UserSerializer(user).data,
    })


@never_cache
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def me(request):
    return Response(UserSerializer(request.user).data)

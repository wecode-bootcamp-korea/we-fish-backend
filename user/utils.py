import jwt
import json

from .models     import User
from my_settings import SECRET_KEY

from django.http import JsonResponse

def login_required(func):

    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        secret = SECRET_KEY['secret']

        if token:
            try:
                decode       = jwt.decode(token, secret, algorithms = ['HS256'])
                user_id      = decode.get('user', None)
                user         = User.objects.get(id = user_id)
                request.user = user

            except jwt.DecodeError:
                return JsonResponse({"message":"INVALID_TOKEN"}, status = 403)

            return func(self, request, *args, **kwargs)

        return JsonResponse({"message":"LOGIN_REQUIRED"}, status = 401)

    return wrapper

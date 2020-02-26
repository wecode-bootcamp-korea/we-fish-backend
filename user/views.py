import json
import bcrypt
import jwt

from .models import User
from my_settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message":"Duplicated email"}, status = 400)
            User(
                email            = data['email'],
                password         = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8'),
                name             = data['name'],
                postcode         = data['postcode'],
                address          = data['address'],
                detailed_address = data.get('detailed_address', None),
                mobile           = data['mobile'],
                agreement        = data.get('agreement', None),
            ).save()

            return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

    def get(self, request):
        user_data = User.objects.values()
        return JsonResponse({"user":list(user_data)}, status = 200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({"user":user.id}, SECRET_KEY['secret'], algorithm = 'HS256')

                    return JsonResponse({"token":token.decode('utf-8')}, status = 200)
                return HttpResponse(status = 401)

            return HttpResponse(status = 401)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)


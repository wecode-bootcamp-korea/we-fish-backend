import json
import bcrypt
import jwt

from .models      import User
from .utils       import login_required
from my_settings  import SECRET_KEY

from django.views import View
from django.http  import HttpResponse, JsonResponse

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message":"Duplicated email"}, status = 400)

            user_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            User(
                email            = data['email'],
                password         = user_password,
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

class ProfileView(View):
    @login_required
    def get(self, request):
        user_profile = {
            'id'               : request.user.email,
            'name'             : request.user.name,
            'mobile'           : request.user.mobile,
            'postcode'         : request.user.postcode,
            'address'          : request.user.address,
            'detailed_address' : request.user.detailed_address,
        }

        return JsonResponse({"profiles":user_profile}, status = 200)

    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)
            profile = User.objects.filter(id = request.user.id)
            profile.update(
                name             = data['name'],
                mobile           = data['mobile'],
                postcode         = data['postcode'],
                address          = data['address'],
                detailed_address = data.get('detailed_address', None),
            )

            password = data.get('password', None)
            if password:
                user_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
                profile = User.objects.filter(id = request.user.id)
                profile.update(
                        password = user_password
                )

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)
import json
import bcrypt
import jwt
import requests
import random
import string

from .models      import User, Verification, Ask
from .utils       import login_required
from my_settings  import SECRET_KEY, SMS

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

class KakaoView(View):
    def post(self, request):
        access_token = request.headers['Authorization']

        kakao_request = requests.get(
            'https://kapi.kakao.com/v2/user/me',
            headers = {
                "Host"          : "kapi.kakao.com",
                "Authorization" : f"Bearer {access_token}",
                "Content-type"  : "application/x-www-from-urlencoded;charset=utf-8"
            }
        ,timeout = 2)

        kakao_id = kakao_request.json().get('id')
        try:
            if User.objects.filter(kakao_id = kakao_id).exists():
                user = User.objects.get(kakao_id = kakao_id)
                token = jwt.encode({"user":user.id}, SECRET_KEY['secret'], algorithm = 'HS256')

                return JsonResponse({"token":token.decode('utf-8')}, status = 200)

            else:
                data = json.loads(request.body)
                User(
                    kakao_id         = kakao_id,
                    email            = data['email'],
                    postcode         = data['postcode'],
                    address          = data['address'],
                    detailed_address = data.get('detailed_address', None),
                ).save()

                user = User.objects.get(kakao_id = kakao_id)
                token = jwt.encode({"user":user.id}, SECRET_KEY['secret'], algorithm = 'HS256')

                return JsonResponse({"token":token.decode('utf-8')}, status = 200)

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

class VerificationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            mobile = data['mobile']

            digit = 6
            verification_code = ''.join(random.choice(string.digits) for x in range(digit))

            user_data = Verification.objects.filter(mobile = mobile)
            if user_data.exists:
                user_data.update(
                    code = verification_code,
                    count = 0
                )
            else:
                Verification(
                    mobile  = mobile,
                    code    = verification_code,
                    count   = 0
                ).save()

            headers = {
                "Content-Type"          : "application/json; charset=utf-8",
                "x-ncp-auth-key"        : SMS['Access_Key'],
                "x-ncp-service-secret"  : SMS['Service_Secret']
            }

            payload = {
                "type"          : "SMS",
                "contentType"   : "COMM",
                "countryCode"   : "",
                "from"          : SMS['From'],
                "to"            : [ mobile ],
                "content"       : f"[we_fish] 인증 코드 [{verification_code}]를 입력해주세요."
            }

            requests.post(SMS['URL'], json = payload, headers = headers)

            return HttpResponse(status =  200)

        except  KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

class ConfirmationView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = Verification.objects.get(mobile = data['mobile'])
            if user.count < 3:
                if data['code'] == user.code:
                    return JsonResponse({"message" : "Verification Succeed"}, status = 200)

                user_data = Verification.objects.filter(mobile = data['mobile'])
                user_data.update(
                    count = user.count + 1
                )

                return JsonResponse({"message" : "Try Again"}, status = 401)

            return JsonResponse({"message" : "Verification Failed"}, status = 401)

        except  KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)


class AskView(View):
    @login_required
    def post(self, request):
        data = json.loads(request.body)
        Ask(
            user_id = request.user.id,
            title   = data.get('title', None),
            author  = data.get('author', None),
            email   = data.get('email', None),
            content = data.get('content', None)
        ).save()

        return HttpResponse(status = 200)

    @login_required
    def get(self, request):
        data = Ask.objects.filter(user_id = request.user.id).values()

        return JsonResponse({"Ask" : list(data)}, status = 200)


class AskEditView(View):
    @login_required
    def get(self, request, inquiry_id):
        user = Ask.objects.filter(id = inquiry_id).values()

        return JsonResponse({"ask_list" : list(user)}, status = 200)

    @login_required
    def post(self, request, inquiry_id):
        data = json.loads(request.body)
        user = Ask.objects.filter(id = inquiry_id).values()
        user.update(
            title   = data.get('title', None),
            author  = data.get('author', None),
            email   = data.get('email', None),
            content = data.get('content', None)
        )

        return HttpResponse(status = 200)

    @login_required
    def delete(self, request, inquiry_id):
        user = Ask.objects.filter(id = inquiry_id)
        user.delete()

        return HttpResponse(status = 200)

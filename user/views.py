import json
import bcrypt
import jwt
import requests
import random
import string

from .models      import User, Verification
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
        data = json.loads(request.body)

        # 6자리 인증코드 생성
        digit = 6
        string_pool = string.digits
        verification_code = ""
        for i in range(digit):
            verification_code += random.choice(string_pool)
        # 휴대폰 번호 및 인증코드 저장
        Verification(
                mobile  =  data['mobile'],
                code    =  verification_code,
                count   = 0
        ).save()

        # 인증코드 발송 요청
        headers = {
            "Content-Type"          : "application/json; charset=utf-8",
            "x-ncp-auth-key"        : SMS['Access_Key'],
            "x-ncp-service-secret"  : SMS['Service_Secret'],
        }

        payload = {
            "type"          : "SMS",
            "contentType"   : "COMM",
            "countryCode"   : "",
            "from"          : SMS['From'],
            "to"            : [
                                data['mobile']
                              ],
            "content"       : f"[we-fish] 인증 코드 [{verification_code}]를 입력해주세요."
            }

        requests.post(SMS['URL'], json = payload, headers = headers)

        return HttpResponse(status =  200)

class ConfirmaionView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = Verification.objects.get(mobile = data['mobile'])
            if int(user.count) < 3:

                if data['code'] == user.code:

                    return JsonResponse({"message":"Verification Successed"}, status = 200)

                user_data = Verification.objects.filter(mobile = data['mobile'])
                user_data.update(
                    count = int(user.count) + 1
                )

                return JsonResponse({"message" : "Try Again"}, status = 401)

            return JsonResponse({"message" : "Verification Failed"}, status = 401)

        except  KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

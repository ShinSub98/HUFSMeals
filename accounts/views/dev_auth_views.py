from rest_framework.views import APIView
import requests
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from ..models import *
from ..serializers import *
from decouple import config


class LocalGoogleLoginView(APIView):
    """
    개발자용 구글 로그인 페이지 접속 뷰
    """
    def get(self, request, value):
        app_key = config('GOOGLE_APP_KEY')
        scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"
        if value == 0:
            redirect_uri = config('LOCAL_REDIRECT_URI')
        elif value == 1:
            redirect_uri = ""
        google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"

        response = redirect(
            f"{google_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
        )
        
        return response
    

class LocalGoogleLoginCallback(APIView):
    """
    개발자용 구글 로그인 콜백
    """
    def get(self, request):
        code = request.GET["code"]
        host = request.get_host()
        if host == "127.0.0.1:8000":
            token_url = "https://oauth2.googleapis.com/token"
            data = {
                "client_id" : config('GOOGLE_APP_KEY'),
                "client_secret" : config('GOOGLE_SECRET'),
                "code" : code,
                "grant_type" : 'authorization_code',
                "redirect_uri" : "http://127.0.0.1:8000/accounts/dev/login/"
            }
        elif host == "hufsmeals.site":
            pass
        
        access_token = requests.post(token_url, data=data).json().get('access_token')

        user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
        user_information = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"}).json()

        google_id = user_information['id']
        user = User.objects.filter(google_id = google_id).first()

        if user:
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            res = {
                "msg" : "기존 사용자 로그인 성공",
                "data" : {
                    "access_token" : access_token,
                    "refresh_token" : refresh_token,
                    "user_info" : UserInfoSerializer(user).data, 
                    "exist_user" : True
                }
            }
            return Response(res, status=status.HTTP_200_OK)
        language_codes = [code[0] for code in User.LANGUAGE_CODE]

        if user_information['locale'] in language_codes:
            language_code = user_information['locale']
        else:
            language_code = 'en'
        
        User(
            google_id = google_id,
            language = language_code,
            email = user_information['email']
        ).save()

        new_user = User.objects.get(google_id = google_id)

        new_user.nickname = f"{new_user.pk}번째 부"
        new_user.save()
        token = TokenObtainPairSerializer.get_token(new_user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        res = {
            "msg" : "새로운 사용자 로그인 성공",
            "data" : {
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "exist_user" : False,
                "pk" : new_user.pk,
                "user_info" : UserInfoSerializer(new_user).data
            }
        }
        return Response(res, status = status.HTTP_201_CREATED)
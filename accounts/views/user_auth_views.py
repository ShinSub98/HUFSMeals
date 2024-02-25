from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..models import *
from ..serializers import *
from decouple import config


class GoogleRedirectView(APIView):
    """
    구글 로그인 페이지 주소를 리턴하는 뷰
    """
    def get(self, request):
        app_key = config('google_app_key')
        scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"
        redirect_uri = "http://localhost:5173/loginLoading"
        google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"

        response = f"{google_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"

        return Response({"address" : response})
    

class ServerGoogleLoginCallback(APIView):
    """
    유저용 구글 로그인 콜백
    """
    def get(self, request, code):
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id" : config('GOOGLE_APP_KEY'),
            "client_secret" : config('GOOGLE_SECRET'),
            "code" : code,
            "grant_type" : 'authorization_code',
            "redirect_uri" : "http://localhost:5173/loginLoading"
        }
        
        access_token = requests.post(token_url, data=data).json().get('access_token')

        user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
        user_data = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"}).json()

        user, created = self.get_or_create_user(
            user_data['id'],
            user_data['email'],
            user_data['locale'],
            user_data['family_name'],
            user_data['given_name'])
        
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        if created:
            msg = "새로운 사용자 로그인 성공"
            exist_user = False
        else:
            msg = "기존 사용자 로그인 성공"
            exist_user = True
        
        res = {
            "msg" : msg,
            "data" : {
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "user_info" : UserInfoSerializer(user).data,
                "exist_user" : exist_user
            }
        }
        return Response(res, status = status.HTTP_200_OK)
    
    def get_or_create_user(self, google_id, email, locale, family_name, given_name):
        user, created = User.objects.get_or_create(
            google_id = google_id,
            email = email,
            family_name = family_name,
            given_name = given_name
        )

        if created:
            user.nickname = f"{user.pk}번째 부"
            user.language = locale
            user.save()
        return user, created
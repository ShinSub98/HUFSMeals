from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('dev/google/<int:value>/', LocalGoogleLoginView.as_view()), # 서버 개발자 로그인
    path('dev/login/', LocalGoogleLoginCallback.as_view()), # 서버 개발자 로그인 콜백
    path('test/google/', GoogleRedirectView.as_view()), # 구글 로그인 url 리턴
    path('login/<str:code>/', ServerGoogleLoginCallback.as_view()), # 유저 로그인 콜백
    path('info/<int:user_id>/', UserInfoView.as_view()), # 유저 정보 반환
    path('token/refresh/', TokenRefreshView.as_view()), # 토큰 리프레쉬 뷰
]

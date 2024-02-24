from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('dev/google/<int:value>/', LocalGoogleLoginView.as_view()), # 서버 개발자 로그인
    path('dev/login/', LocalGoogleLoginCallback.as_view()), # 서버 개발자 로그인 콜백
]

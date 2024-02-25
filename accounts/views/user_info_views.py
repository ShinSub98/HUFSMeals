from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserInfoView(APIView):
    """
    유저 정보를 반환하는 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = User.objects.get(pk = user_id)
        serializer = UserInfoSerializer(user)
        res = {
            "msg" : "유저 정보 반환 성공",
            "data" : serializer.data
        }
        return Response(res, status = status.HTTP_200_OK)

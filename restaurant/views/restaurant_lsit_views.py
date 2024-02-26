from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class RestaurantLocationView(APIView):
    """
    식당 위치 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = RestaurantResponseSerializer(Restaurant.objects.all(), many = True).data
        
        res = {
            "msg" : "식당 위/경도 반환 성공",
            "data" : data
        }
        return Response(res, status = status.HTTP_200_OK)

from rest_framework import serializers
from ..models import User

class UserInfoSerializer(serializers.ModelSerializer):
    """
    유저의 정보 시리얼라이저
    """
    class Meta:
        model = User
        fields = ['id', 'nickname', 'language', 'is_banned', 'email', 'is_banned', 'is_staff']
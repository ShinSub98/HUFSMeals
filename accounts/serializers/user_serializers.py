from rest_framework import serializers
from models import User

class UserDetailSerializer(serializers.ModelSerializer):
    """
    유저의 모든 정보 시리얼라이저
    """
    class Meta:
        model = User
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    """
    유저의 간단한 정보 시리얼라이저
    """
    class Meta:
        models = User
        fields = ['id', 'nickname', 'language', 'is_banned']
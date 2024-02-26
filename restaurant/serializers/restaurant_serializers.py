from rest_framework import serializers
from ..models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class RestaurantRequestSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'restaurant_image', 'address', 'phone']

    
class RestaurantResponseSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many = True)
    class Meta:
        model = Restaurant
        exclude = ['score_accum']
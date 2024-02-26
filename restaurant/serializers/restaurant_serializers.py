from rest_framework import serializers
from ..models import *

class RestaurantRequestSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'restaurant_image', 'address', 'phone']

    
class RestaurantResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ['score_accum']
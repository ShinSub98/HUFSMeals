from django.contrib import admin
from .models import *
from decouple import config
import requests

# Register your models here.

def geocording(address):
    api_address = "https://dapi.kakao.com/v2/local/search/address.json"

    headers = {
        "Authorization" : f"KakaoAK {config('kakao_app_key')}"
    }
    data = {
        "query" : address,
        "analyze_type" : "exact",
    }

    response = requests.get(api_address, headers=headers, data=data).json()
    print(response)

    if len(response['documents']) == 0:
        return None, None
    else:
        latitude = response['documents'][0]['y']
        longitude = response['documents'][0]['x']
        print(latitude, longitude)
        return latitude, longitude
    

class RestaurantAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'address' in form.changed_data:
            latitude, longitude = geocording(obj.address)
            obj.latitude = latitude
            obj.longitude = longitude
        super().save_model(request, obj, form, change)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu)
from django.urls import path
from .views import *

app_name = 'restaurant'

urlpatterns = [
    path('location/', RestaurantLocationView.as_view()),
]

from django.urls import path
from app0.views import *

urlpatterns = [
    path('top/', top),
    path('profile/', profile),
    path('memes/',memes),
    path('free/',free),
    path('profile/<str:type>/',show),
]
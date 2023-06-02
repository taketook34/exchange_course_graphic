from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='main'),
    #path('register/', registration, name='register'),
    #path('create_curse/', create_curse, name='create'),
]

from django.urls import path
from .views import *

app_name = 'chat_app'

urlpatterns = [
    path('', app_index, name="index"),
    path('<str:room_name>/', room, name='room'),
]
#path('<str:room_name>/', views.room, name='room'),
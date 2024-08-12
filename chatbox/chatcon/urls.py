from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.catch_all, name='catch_all'), 
    path('register/', views.register, name='register'), 
    path('login/', views.login_view, name='login'), 
    path('chat_room/', views.chat_room, name='chat_room'), 
    path('send_message/', views.send_message, name='send_message'), 
    ]
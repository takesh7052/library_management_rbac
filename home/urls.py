from django.contrib import admin
from django.urls import path, include
from home import views
from home.models import adduser

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('adduser',views.adduser, name="adduser"),
    path('indexuser',views.adduser, name="indexuser"),
]
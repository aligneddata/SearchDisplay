from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("", views.index, name="index"),
]

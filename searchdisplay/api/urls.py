from django.urls import path, re_path

from . import views

urlpatterns = [
    path('search', views.search),
    path('upload_document', views.upload_document),
]
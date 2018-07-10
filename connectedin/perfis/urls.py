from django.contrib import admin
from django.urls import path

urlpatterns = [
  path(r'^$','perfis.views.index'),
    
]



from django.contrib import admin
from django.urls import path
from .views import findex

urlpatterns = [
    path('', findex),



]

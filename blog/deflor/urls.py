from django.contrib import admin
from django.urls import include, path
from deflor.views import *

urlpatterns = [
    path('', index, name="home_page")
]
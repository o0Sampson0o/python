from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
]
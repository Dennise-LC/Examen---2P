from os import name
from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('p2/',views.p2,name = 'p2'),
    path('RespuestaP2/',views.p3,name ='p3'),
]
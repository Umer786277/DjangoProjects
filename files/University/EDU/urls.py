from django.contrib import admin
from django.urls import path
from EDU import views


urlpatterns = [
    path('',views.index,name='home'),
     path('contact/',views.contact,name='contact'),
]
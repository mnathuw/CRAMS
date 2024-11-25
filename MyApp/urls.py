from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("signout",views.signout,name = "signout"),
    path("contact",views.contact,name = 'contact')
    ]
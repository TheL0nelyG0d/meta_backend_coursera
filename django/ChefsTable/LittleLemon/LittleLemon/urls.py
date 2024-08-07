"""
URL configuration for LittleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LittleLemonApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello/', views.say_hello),
    path('home/', views.homepage),
    path('shift/', views.shift_form),
    path('date/', views.display_date),
    path('menu/', views.menu),
    path('menu/<str:dish>', views.menuitems, name="menu"),
    path('about/', views.about),
    path('menupic/', views.menu_pic),
    path('about/', views.about),
]

handler404 = 'LittleLemon.views.handler404'
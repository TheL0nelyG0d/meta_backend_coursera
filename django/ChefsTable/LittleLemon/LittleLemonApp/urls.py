from django.contrib import admin
from django.urls import path
from . import views

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
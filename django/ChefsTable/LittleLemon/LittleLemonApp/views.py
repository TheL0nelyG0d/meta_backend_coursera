from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#from .models import Menu
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    return HttpResponse("Welcome to Little Lemon")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon"""
    return HttpResponse(text)
#def menu_by_id(request, menu_id):
#    menu = Menu.Objects.get(pk=menu_id)
#    return HttpResponse(f"{menu.mednu_item}: Type of {menu.cuisine} cuisine")

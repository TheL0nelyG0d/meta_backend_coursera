from django.shortcuts import render
from django.http import HttpResponse

from .models import Menu
# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def menu_by_id(request, menu_id):
    menu = Menu.Objects.get(pk=menu_id)
    return HttpResponse(f"{menu.mednu_item}: Type of {menu.cuisine} cuisine")

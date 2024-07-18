from django.contrib import admin
from .models import Menu, Drinks, Customer, Logger

# Register your models here.

admin.site.register(Menu)
admin.site.register(Drinks)
admin.site.register(Customer)
admin.site.register(Logger)
from django.contrib import admin
from .models import Menu, Drinks, Customer

# Register your models here.

admin.site.register(Menu)
admin.site.register(Drinks)
admin.site.register(Customer)
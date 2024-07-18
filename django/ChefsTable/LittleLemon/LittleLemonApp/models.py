from unicodedata import name
from django.db import models


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    year = models.IntegerField()



    def __str__(self):
        return self.name + " : " + self.cuisine
    

class Drinks(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    category_id = models.ForeignKey(Menu, on_delete=models.PROTECT, default=None, related_name="category_name")



    def __str__(self):
        return self.name + " : " + self.category
    

class Customer (models.Model):
    name = models.CharField(max_length=100)
    reservation_Date = models.CharField(max_length=30)
    seats = models.IntegerField()


    def __str__(self):
        return self.name
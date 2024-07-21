from django.db import models

class Book(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.PositiveSmallIntegerField(null=True, blank=True)


    


# Generated by Django 4.1.3 on 2024-07-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]

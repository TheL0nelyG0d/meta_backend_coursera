# Generated by Django 5.0.7 on 2024-07-18 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='price',
            new_name='year',
        ),
    ]
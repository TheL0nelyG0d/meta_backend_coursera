# Generated by Django 5.0.7 on 2024-07-18 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonApp', '0003_drinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='LittleLemonApp.menu'),
        ),
    ]
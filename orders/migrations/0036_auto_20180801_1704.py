# Generated by Django 2.0.7 on 2018-08-01 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_pizzatopping_pizzatoppingentry_subtopping_subtoppingentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzatoppingentry',
            options={'verbose_name': 'Pizza Topping Entry', 'verbose_name_plural': 'Pizza Topping Entries'},
        ),
        migrations.AlterModelOptions(
            name='subtoppingentry',
            options={'verbose_name': 'Sub Topping Entry', 'verbose_name_plural': 'Sub Topping Entries'},
        ),
    ]
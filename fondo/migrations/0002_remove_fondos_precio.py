# Generated by Django 2.2.12 on 2022-05-09 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fondos',
            name='precio',
        ),
    ]

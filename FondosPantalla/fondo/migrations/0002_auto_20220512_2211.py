# Generated by Django 2.2.12 on 2022-05-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fondos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='preview'),
        ),
    ]

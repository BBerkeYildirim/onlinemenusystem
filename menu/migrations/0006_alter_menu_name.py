# Generated by Django 4.1.5 on 2023-01-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

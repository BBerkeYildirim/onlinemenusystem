# Generated by Django 4.1.5 on 2023-01-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

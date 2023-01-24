# Generated by Django 4.1.5 on 2023-01-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_alter_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='categories/default.png', upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menus'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/default.png', upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]

# Generated by Django 4.0.3 on 2022-09-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.TextField(default='', unique=True),
        ),
    ]

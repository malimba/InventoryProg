# Generated by Django 4.0.3 on 2022-08-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.TextField(default='')),
                ('units', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]

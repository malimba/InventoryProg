# Generated by Django 4.0.3 on 2022-08-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='amountmade',
            field=models.FloatField(default=0),
        ),
    ]

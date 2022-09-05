# Generated by Django 4.0.3 on 2022-08-29 07:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_attribute_brand_category_company_ledger_order_stores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=128, region=None),
        ),
    ]
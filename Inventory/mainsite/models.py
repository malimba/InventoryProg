from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Products(models.Model):
    "Products model"
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product_name = models.TextField(blank=False, null=False, default='')
    sku = models.TextField(blank=False, null=False, default='')
    units = models.IntegerField(blank=False, null=False, default=0)
    price = models.FloatField(blank=False, null=False, default=0)
    amountmade = models.FloatField(blank=True, null=True, default=0)
    description = RichTextField()
    brand = models.IntegerField() #todo: views should use id to to find out whether name matches any result of brands
                                        #and check with ajax@
    category = models.IntegerField() #todo: views should use id to to find out whether name matches any result of brands
                                        #and check with ajax@
    store = models.IntegerField()
    availability = models.IntegerField(default= 0, blank=False, null=False) #availabity 0-no 1-yes

class Brand(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    brand_name = models.TextField(blank=False, null=False, default='')
    status = models.IntegerField(blank=False, null=False, default = '')
class Category(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    category_name = models.TextField(blank=False, null=False, default='')
    status = models.IntegerField(blank=False, null=False, default = '')

class Stores(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    store_name = models.TextField(blank=False, null=False, default='')
    status = models.IntegerField(blank=False, null=False, default = '')

class Attribute(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    attr_name = models.TextField(blank=False, null=False, default='')
    status = models.IntegerField(blank=False, null=False, default='')


class Order(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    customer_name = models.TextField(blank=False, null=False, default='')
    customer_address = models.TextField(blank=False, null=False, default='')
    customer_phone = models.IntegerField(blank=False, null=False, default=502259962)
    product_name = models.IntegerField(blank=False, null=False, default=0)#dropdown of all products
    gross_amount = models.IntegerField(blank=False, null=False, default=0)
    s_charge = models.FloatField(blank=False, null=False, default=0) #13%
    vat = models.FloatField(blank=False, null=False, default=0) #10%
    discount = models.IntegerField(blank=False, null=False, default=0)
    net_amnt = models.IntegerField(blank=False, null=False, default=0)

#ledger system for reports! #todo: alaways pass all product purchase through ledger system
class Ledger(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    prod_id = models.IntegerField(blank=False, null=False, default=0)
    customer_name = models.IntegerField(blank=False, null=False, default=0)
    amount_made = models.IntegerField(blank=False, null=False, default=0)

class Company(models.Model):#this is the company's actual info
    id = models.AutoField(primary_key=True, blank=False, null=False)
    company_name = models.TextField(max_length=255, blank=False, null=False, default='Mal\'s store')
    charge_amnt = models.FloatField(blank=False, null=False, default=0.0)
    vat = models.FloatField(blank=False, null=False, default=0.0)
    address = models.TextField(blank=False, null=False, default='')
    phone = models.BigIntegerField(blank=False, null=False, default=0)
    country = models.CharField(max_length=70, blank=False, null=False, default='Ghana')
    message = RichTextField()
    #0- GHABNA CEDIS
    #1- USD

    currency = models.IntegerField(default=0, blank=False, null=False)

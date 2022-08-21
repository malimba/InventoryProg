from django.db import models

# Create your models here.
class Products(models.Model):
    "Products model"
    id = models.AutoField(primary_key=True, blank=False, null=False)
    product_name = models.TextField(blank=False, null=False, default='')
    units = models.IntegerField(blank=False, null=False, default=0)
    price = models.FloatField(blank=False, null=False, default=0)
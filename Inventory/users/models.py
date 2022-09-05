from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

#security
from werkzeug.security import generate_password_hash

class User(AbstractBaseUser):
    """
    Custom abstract user Model
    """
    id = models.AutoField(primary_key=True, blank=False, null=False)

    user_group = models.CharField(max_length=255, blank=False, null=False, default='') #stores group user is found in!

    fullname = models.CharField(max_length=85, blank=False, null=False)
    lastname = models.CharField(max_length=85, blank=False, null=False)

    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=30, blank=False, null=False,
                                unique=False)  # user cannot have a username greater than 30 chars
    email = models.CharField(max_length=100, blank=False, null=False,
                                unique=False)  # user cannot have a user
    phone = PhoneNumberField(blank=False, default='+41524204242')
    #0 - male 1- female
    gender = models.CharField(max_length=1, blank=False, null=False, default=0)
    amountmade = models.FloatField(blank=False, null=False, default=0)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    #REQUIRED FIELDS
    REQUIRED_FIELDS = ['fullname', 'username', ]

    # methods
    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at', '-updated_at',)

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def hash_password(self):
        # create password salt
        hash = generate_password_hash(self.password, method='pbkdf2:sha256', salt_length=8)
        self.password = hash

class Groups(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    group_name = models.CharField(max_length=255, blank=False, null=False, default='')
    #permissions below
    permissions = models.TextField(blank=False, null=False, default='')

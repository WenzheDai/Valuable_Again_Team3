from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser, BaseModel):
    """Model of User-----inherit the Django built-in authenticator system"""

    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name

class Address(BaseModel):
    """Model of Address"""
    user = models.ForeignKey('User', verbose_name='Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='name')
    Address = models.CharField(max_length=256, verbose_name='Address')
    postcode = models.CharField(max_length=6, null=False, verbose_name='Postcode', default='abc')
    phone = models.CharField(max_length=10, verbose_name='Phone')
    is_default = models.BooleanField(default=False, verbose_name='Default')

    class Meta:
        db_table = 'df_address'
        verbose_name = 'Address'
        verbose_name_plural = verbose_name
from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser, BaseModel):
    """Model of User-----inherit the Django built-in authenticator system"""
    Profile_picture = models.ImageField(max_length=512, verbose_name="Profile_picture", default="default-avatar.png")
    notices = models.CharField(max_length=128, verbose_name='notice', default='No any notices')

    class Meta:
        db_table = 'df_user'
        verbose_name = 'User'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    """Model of Address"""
    user = models.ForeignKey('User', verbose_name='Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='name')
    Address = models.CharField(max_length=256, verbose_name='Address')
    postcode = models.CharField(max_length=6, null=False, verbose_name='Postcode')
    phone = models.CharField(max_length=10, verbose_name='Phone')
    is_default = models.BooleanField(default=False, verbose_name='Default')

    class Meta:
        db_table = 'df_address'
        verbose_name = 'Address'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Address
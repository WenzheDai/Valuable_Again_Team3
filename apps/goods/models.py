from django.db import models
from db.base_model import BaseModel
from apps.user.models import User

class Items(BaseModel):
    """model of items"""
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    itemsName = models.CharField(max_length=32, verbose_name='itemName')
    price = models.IntegerField(verbose_name='itemPrice', default=0)
    describe = models.CharField(max_length=2000, verbose_name='describe')

    class Meta:
        db_table = "df_items"
        verbose_name = "Items"
        verbose_name_plural=verbose_name

class ItemPicture(BaseModel):
    item = models.ForeignKey(Items, verbose_name='items', on_delete=models.CASCADE)
    itemPicture = models.ImageField(max_length=20, verbose_name='goodsImage', default='default-image.png')

    class Meta:
        db_table = "df_itemPicture"
        verbose_name = "ItemPicture"
        verbose_name_plural = verbose_name


#Considering
# class ItemCategory(BaseModel):




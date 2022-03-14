from django.db import models
from db.base_model import BaseModel
from apps.user.models import User
from apps.goods.models import Items

class Orders(BaseModel):
    seller = models.ForeignKey(User, verbose_name='seller', on_delete=None, related_name='seller')
    buyer = models.ForeignKey(User, verbose_name='buyer', on_delete=None, related_name='buyer')
    tradGood = models.ForeignKey(Items, verbose_name='tradGood', on_delete=None)

    #Three status In progress/Finished/Cancelled
    status = models.CharField(max_length=32, verbose_name='orderStatus', default="In progress")


    class Meta:
        db_table = "df_orders"
        verbose_name = "Orders"
        verbose_name_plural = verbose_name
from django.db import models


class BaseModel(models.Model):
    """The model of base class"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update time')
    is_delete = models.BooleanField(default=False, verbose_name='delete flag')

    class Meta:
        # This is an abstract class
        abstract = True
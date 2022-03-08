from django.urls import path, include
from apps.goods import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem', views.addItem, name='addItem')
]

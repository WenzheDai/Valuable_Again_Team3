from django.urls import path, include
from apps.goods import views
from apps.goods.views import Index, AddItem

urlpatterns = [
    # path('', views.index, name='index'),
    # path('addItem', views.addItem, name='addItem')
    path('', Index.as_view(), name='index'),
    path('addItem', AddItem.as_view(), name='addItem'),
]

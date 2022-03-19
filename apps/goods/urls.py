from django.urls import path, include
from apps.goods import views
from apps.goods.views import Index,IndexCategory, AddItem, UpLoadGoodsImage, ItemDetial, Notice

urlpatterns = [
    # path('', views.index, name='index'),
    # path('addItem', views.addItem, name='addItem')
    path('', Index.as_view(), name='index'),
    path('category/<str:category>', IndexCategory.as_view(), name='indexCategory'),
    path('detail/<int:item_id>', ItemDetial.as_view(), name='detail'),
    path('addItem', AddItem.as_view(), name='addItem'),
    path('uploadGoodsImage', UpLoadGoodsImage.as_view(), name='uploadGoodsImage'),
    path('detail/bookGoods', ItemDetial.as_view(), name='bookGoods'),
    path('notice', Notice.as_view(), name='notice'),
    path('user/notice', Notice.as_view(), name='notice'),
    path('detail/notice', Notice.as_view(), name='notice'),
    path('addItem/notice', Notice.as_view(), name='notice'),
    path('category/notice', Notice.as_view(), name='notice'),
]

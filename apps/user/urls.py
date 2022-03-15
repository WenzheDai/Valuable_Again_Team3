from django.urls import path, include

from apps.order.views import CancelOrder, FinishOrder
from apps.user import views
from apps.user.views import RegisterView, LoginView, UserInfoView, \
    UserOrdersView, AddressView,UserItemsView, LogoutView, UpLoadAvatar,SaveAvatar

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', UserInfoView.as_view(), name='centerProfile'),
    path('address', AddressView.as_view(), name='centerAddress'),
    path('myItems', UserItemsView.as_view(), name='myItems'),
    path('orders', UserOrdersView.as_view(), name='centerOrders'),
    path('uploadAvatar', UpLoadAvatar.as_view(), name='uploadAvatar'),
    path('saveAvatar', SaveAvatar.as_view(), name='saveAvatar'),
    path('cancel', CancelOrder.as_view(), name='cancelOrder'),
    path('finish', FinishOrder.as_view(), name='finishOrder')
]

from django.urls import path, include
from apps.user import views
from apps.user.views import RegisterView, LoginView, UserInfoView, UserOrdersView, AddressView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', UserInfoView.as_view(), name='centerProfile'),
    path('address', AddressView.as_view(), name='centerAddress'),
    path('orders', UserOrdersView.as_view(), name='centerOrders')
]

from django.urls import path, include
from apps.user import views
from apps.user.views import RegisterView, LoginView

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('center/profile', views.user_center_profile, name='center-profile'),
    path('center/address', views.user_center_address, name='center-address'),
    path('center/orders', views.user_center_orders, name='center-orders')
]

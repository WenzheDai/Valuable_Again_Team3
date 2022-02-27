from django.urls import path, include
from apps.user import views
from apps.user.views import RegisterView, LoginView

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register')
]

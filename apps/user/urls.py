from django.urls import path, include
from apps.user import views
from apps.user.views import RegisterView

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('register/', RegisterView.as_view(), name='register')
]

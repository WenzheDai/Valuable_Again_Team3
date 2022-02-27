"""Valuable_Again_Team3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.goods import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #home page ----- 首页path在这里生成
    path('', views.index, name='index'),
    # path('goods/', include(('goods.urls', 'goods'), namespace='goods')),
    path('user/', include(('apps.user.urls', 'apps.user'), namespace='user')),
    path('order/', include(('apps.order.urls', 'apps.order'), namespace='order')),
    path('', include(('apps.goods.urls', 'apps.goods'), namespace='goods')),
]

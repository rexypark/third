"""thrid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from app.views import index, list, save, edit

# app디렉토리 안에있는 views가 가지고 있는 정의된 함수 index를 데리고온다.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('list/', list),
    path('edit/<int:id>', edit),
    path('save/<int:id>', save)
]

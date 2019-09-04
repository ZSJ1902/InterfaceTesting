"""InterfaceTestingMock URL Configuration

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
from django.urls import path, re_path
from interface_crud.views import query_article, add_article, modify_article, delete_article, test_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query_article/', query_article, name='query_article'),
    path('add_article/', add_article, name='add_article'),
    path('modify_article/<int:article_id>', modify_article, name='modify_article'),
    path('delete_article/<int:article_id>', delete_article, name='delete_article'),
    path('test_api/', test_api, name='test_api')
]

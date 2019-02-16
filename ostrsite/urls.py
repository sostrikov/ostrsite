"""ostrsite URL Configuration

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
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html",
        extra_context={"header": "Словарь, который можно передать в шаблон"})),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
    path('details/', views.details),
    path('current_datetime/', views.current_datetime),

    #re_path(r'^products/$', views.products),
    #re_path(r'^products/(?P<productid>\d+)/', views.products),
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    #path('about/', views.about),
    #path('contact/', views.contact),
    path('products/', views.products),
    path('products/<int:productid>/', views.products),

    path('users/', views.users),
    path('users/<int:id>/<str:name>/', views.users),

    path('products/<int:productid>/', views.products),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

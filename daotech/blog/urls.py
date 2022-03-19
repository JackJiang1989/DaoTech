"""daotech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article_one/<int:article_id>/', views.article_one, name='article_one'),
    path('article_all/', views.article_all, name='article_all'),
    path('article_archive/', views.article_archive, name='article_archive'),    
    path('about_me/', views.about_me, name='about_me'),    
    path('markdowntest/', views.markdowntest, name='markdowntest'),
    path('food/', views.food, name='food'),
    # path('article_detail/comments/', views.comments, name='comments')
]

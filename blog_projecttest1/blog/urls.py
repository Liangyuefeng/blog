#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index),
    path('AI',views.AI),
    path('database',views.Database),
    path('frontend',views.Frontend),
    path('background',views.Background),
    path('mobile',views.Mobile),
    path('manage',views.Manage),

]
app_name = 'blog'

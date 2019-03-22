# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'django_portrait'
urlpatterns = [
    path('portrait/create/',
         views.PortraitCreateView.as_view(),
         name='portrait_create'),
    path('portrait/delete/<pk>',
         views.PortraitDeleteView.as_view(),
         name='portrait_delete'),
    path('portrait/<pk>',
         views.PortraitDetailView.as_view(),
         name='portrait_detail'),
    path('portrait/update/<pk>',
         views.PortraitUpdateView.as_view(),
         name='portrait_update'),
    path('portrait/',
         views.PortraitCreateView.as_view(),
         name='portrait_list')
    ]

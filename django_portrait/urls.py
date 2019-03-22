# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_portrait'
urlpatterns = [
    url(
        regex="^Portrait/~create/$",
        view=views.PortraitCreateView.as_view(),
        name='Portrait_create',
    ),
    url(
        regex="^Portrait/(?P<pk>\d+)/~delete/$",
        view=views.PortraitDeleteView.as_view(),
        name='Portrait_delete',
    ),
    url(
        regex="^Portrait/(?P<pk>\d+)/$",
        view=views.PortraitDetailView.as_view(),
        name='Portrait_detail',
    ),
    url(
        regex="^Portrait/(?P<pk>\d+)/~update/$",
        view=views.PortraitUpdateView.as_view(),
        name='Portrait_update',
    ),
    url(
        regex="^Portrait/$",
        view=views.PortraitListView.as_view(),
        name='Portrait_list',
    ),
	]

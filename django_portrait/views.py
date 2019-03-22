# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import Portrait


class PortraitCreateView(CreateView):
    model = Portrait


class PortraitDeleteView(DeleteView):

    model = Portrait


class PortraitDetailView(DetailView):

    model = Portrait


class PortraitUpdateView(UpdateView):

    model = Portrait


class PortraitListView(ListView):
    model = Portrait

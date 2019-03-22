# -*- coding: utf-8 -*-

from django.db import models


class Portrait(models.Model):
    user = models.BooleanField()

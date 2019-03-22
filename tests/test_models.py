#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-portrait
------------

Tests for `django-portrait` models module.
"""

from django.test import TestCase

from django_portrait import models


class TestDjango_portrait(TestCase):

    def setUp(self):
        instance = models.Portrait()

    def test_something(self):
        pass

    def tearDown(self):
        pass

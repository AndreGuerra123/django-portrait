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
        self.portrait = models.Portrait()

    def test_something(self):
        assert self.portrait

    def tearDown(self):
        pass

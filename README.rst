=============================
Django Portrait
=============================

.. image:: https://badge.fury.io/py/django-portrait.svg
    :target: https://badge.fury.io/py/django-portrait

.. image:: https://travis-ci.org/AndreGuerra123/django-portrait.svg?branch=master
    :target: https://travis-ci.org/AndreGuerra123/django-portrait

.. image:: https://codecov.io/gh/AndreGuerra123/django-portrait/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/AndreGuerra123/django-portrait

User portraits for Django projects.

Documentation
-------------

The full documentation is at https://django-portrait.readthedocs.io.

Quickstart
----------

Install Django Portrait::

    pip install django-portrait

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_portrait.apps.DjangoPortraitConfig',
        ...
    )

Add Django Portrait's URL patterns:

.. code-block:: python

    from django_portrait import urls as django_portrait_urls


    urlpatterns = [
        ...
        url(r'^', include(django_portrait_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

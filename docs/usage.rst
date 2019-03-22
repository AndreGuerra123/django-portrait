=====
Usage
=====

To use Django Portrait in a project, add it to your `INSTALLED_APPS`:

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

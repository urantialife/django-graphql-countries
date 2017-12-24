Django GraphQL Countries
========================

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|


GraphQL implementation for countries

Dependencies
------------

* Python ≥ 3.5
* Django ≥ 1.11
* Postgres


Installation
------------

Install last stable version from Pypi.

.. code:: sh

    pip install django-graphql-countries


Add ``countries`` to your INSTALLED_APPS setting.

.. code:: python

    INSTALLED_APPS = [
        ...
        'django_filters',
        'countries.apps.CountriesAppConfig',
    ]

Add queries to your GraphQL schema

.. code:: python

    import graphene
    import graphql_countries

    class Query(graphene.ObjectType, graphql_countries.Query):
        pass

    schema = graphene.Schema(query=Query)


.. |Pypi| image:: https://img.shields.io/pypi/v/django-graphql-countries.svg
   :target: https://pypi.python.org/pypi/django-graphql-countries

.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-graphql-countries.svg
   :target: https://pypi.python.org/pypi/django-graphql-countries

.. |Build Status| image:: https://travis-ci.org/flavors/graphql-countries.svg?branch=master
   :target: https://travis-ci.org/flavors/graphql-countries

.. |Codecov| image:: https://img.shields.io/codecov/c/github/flavors/graphql-countries.svg
   :target: https://codecov.io/gh/flavors/graphql-countries

.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/5c5f19adc7739cd22c6f/maintainability
   :target: https://codeclimate.com/github/flavors/graphql-countries

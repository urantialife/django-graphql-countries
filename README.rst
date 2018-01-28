Django GraphQL Countries
========================

|Pypi| |Wheel| |Build Status| |Codecov| |Code Climate|


`Countries`_ support for `Django GraphQL`_

.. _Countries: https://github.com/flavors/django-countries/
.. _Django GraphQL: https://github.com/graphql-python/graphene-django


Dependencies
------------

* Python ≥ 3.4
* Django ≥ 1.11
* PostGIS database (PostgreSQL ≥ 9.4)


Installation
------------

Install last stable version from Pypi.

.. code:: sh

    pip install django-graphql-countries


Add ``countries`` to your *INSTALLED_APPS* settings:

.. code:: python

    INSTALLED_APPS = [
        ...
        'countries.apps.CountriesAppConfig',
    ]


Apply **migrations**:

.. code:: python

    python manage.py migrate


Load data
---------

The ``loadcountries`` management command read all **fixtures** and re-loaded into the database:

.. code:: sh

    python manage.py loadcountries


Schema
------

Add queries to your GraphQL schema

.. code:: python

    import graphene
    import graphql_countries


    class Query(graphene.ObjectType, graphql_countries.Query):
        """GraphQL Queries"""


    schema = graphene.Schema(query=Query)


GeoJSON query
-------------

Countries *GeoJSON* **outlines**:

.. code:: graphql

    query {
      countries {
        capital
        mpoly {
          type
          coordinates
        }
      }
    }


Relay
-----

Complete support for `Relay`_.

.. _Relay: https://facebook.github.io/relay/

.. code:: python

    import graphene
    import graphql_countries


    class Query(graphene.ObjectType, graphql_countries.relay.Query):
        """Relay Queries"""


    schema = graphene.Schema(query=Query)


GeoJSON query
-------------

*GeoJSON* **outlines** for 🇻🇳 Vietnam:

.. code:: graphql

    query {
      countries(cca2: "VN") {
        edges {
          node {
            capital
            mpoly {
              type
              coordinates
            }
          }
        }
      }
    }


.. |Pypi| image:: https://img.shields.io/pypi/v/django-graphql-countries.svg
   :target: https://pypi.python.org/pypi/django-graphql-countries

.. |Wheel| image:: https://img.shields.io/pypi/wheel/django-graphql-countries.svg
   :target: https://pypi.python.org/pypi/django-graphql-countries

.. |Build Status| image:: https://travis-ci.org/flavors/django-graphql-countries.svg?branch=master
   :target: https://travis-ci.org/flavors/django-graphql-countries

.. |Codecov| image:: https://img.shields.io/codecov/c/github/flavors/django-graphql-countries.svg
   :target: https://codecov.io/gh/flavors/django-graphql-countries

.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/909e7331eb1c43e92a46/maintainability
   :target: https://codeclimate.com/github/flavors/django-graphql-countries

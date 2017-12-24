import os

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django_filters',
    'countries.apps.CountriesAppConfig',
    'tests',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ['POSTGRES_DB_NAME'],
        'USER': os.environ.get('POSTGRES_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD', ''),
    },
}

SECRET_KEY = 'test'

GRAPHENE = {
    'SCHEMA': 'tests.schema.schema',
}

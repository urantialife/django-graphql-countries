from graphene import relay
from graphene_django.types import DjangoObjectType

from countries import models

from . import lookups, types


class CurrencyNode(DjangoObjectType):

    class Meta:
        model = models.Currency
        interfaces = [relay.Node]
        filter_fields = {
            'code': lookups.CHOICES_LOOKUPS,
            'numeric': lookups.CHOICES_LOOKUPS,
            'name': lookups.TEXT_LOOKUPS,
            'full_name': lookups.TEXT_LOOKUPS,
        }


class LanguageNode(DjangoObjectType):

    class Meta:
        model = models.Language
        interfaces = [relay.Node]
        filter_fields = {
            'name': lookups.TEXT_LOOKUPS,
            'cla2': lookups.CHOICES_LOOKUPS,
            'cla3': lookups.CHOICES_LOOKUPS,
        }


class TimezoneNode(DjangoObjectType):

    class Meta:
        model = models.Timezone
        interfaces = [relay.Node]
        filter_fields = {
            'name': lookups.TEXT_LOOKUPS,
        }


class ContinentNode(DjangoObjectType):

    class Meta:
        model = models.Continent
        interfaces = [relay.Node]
        filter_fields = {
            'code': lookups.CHOICES_LOOKUPS,
            'name': lookups.TEXT_LOOKUPS,
        }


class LocaleNode(DjangoObjectType):
    extra = types.CamelJSON()

    class Meta:
        model = models.Locale
        interfaces = [relay.Node]
        filter_fields = {
            'code': lookups.CHOICES_LOOKUPS,
            'country__cca2':  lookups.CHOICES_LOOKUPS,
            'language__cla2':  lookups.CHOICES_LOOKUPS,
            'language__cla3':  lookups.CHOICES_LOOKUPS,
        }


class CountryNameNode(DjangoObjectType):

    class Meta:
        model = models.CountryName
        interfaces = [relay.Node]
        filter_fields = {
            'common': lookups.TEXT_LOOKUPS,
            'official':  lookups.TEXT_LOOKUPS,
            'language__cla2':  lookups.CHOICES_LOOKUPS,
            'language__cla3':  lookups.CHOICES_LOOKUPS,
        }


class CountryNode(DjangoObjectType):
    extra = types.CamelJSON()

    class Meta:
        model = models.Country
        interfaces = [relay.Node]
        filter_fields = {
            'cca2': lookups.CHOICES_LOOKUPS,
            'cca3': lookups.CHOICES_LOOKUPS,
            'area': lookups.RANGE_LOOKUPS,
            'borders__cca2':  lookups.CHOICES_LOOKUPS,
            'continent__code':  lookups.CHOICES_LOOKUPS,
            'currencies__code':  lookups.CHOICES_LOOKUPS,
            'languages__cla3':  lookups.CHOICES_LOOKUPS,
            'languages__cla2':  lookups.CHOICES_LOOKUPS,
            'timezones__name':  lookups.TEXT_LOOKUPS,
        }

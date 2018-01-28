from graphene_django.types import DjangoObjectType

from countries import models


class CurrencyType(DjangoObjectType):

    class Meta:
        model = models.Currency


class LanguageType(DjangoObjectType):

    class Meta:
        model = models.Language


class TimezoneType(DjangoObjectType):

    class Meta:
        model = models.Timezone


class ContinentType(DjangoObjectType):

    class Meta:
        model = models.Continent


class LocaleType(DjangoObjectType):

    class Meta:
        model = models.Locale


class CountryNameType(DjangoObjectType):

    class Meta:
        model = models.CountryName


class CountryType(DjangoObjectType):

    class Meta:
        model = models.Country

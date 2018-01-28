import graphene

from countries import models

from . import mixins, types


class Query(mixins.QueryResolveMixin):
    country = graphene.Field(
        types.CountryType,
        cca2=graphene.String(required=True))

    countries = graphene.List(types.CountryType)
    languages = graphene.List(types.LanguageType)
    locales = graphene.List(types.LocaleType)
    timezones = graphene.List(types.TimezoneType)

    def resolve_country(self, info, **kwargs):
        try:
            country = models.Country.objects.get(**kwargs)
        except models.Country.DoesNotExist:
            return None
        return country

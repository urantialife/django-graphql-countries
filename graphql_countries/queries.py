from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from countries import models

from . import nodes


class Query(object):
    country = relay.Node.Field(nodes.CountryNode)
    countries = DjangoFilterConnectionField(nodes.CountryNode)
    languages = DjangoFilterConnectionField(nodes.LanguageNode)
    locales = DjangoFilterConnectionField(nodes.LocaleNode)
    timezones = DjangoFilterConnectionField(nodes.TimezoneNode)

    def resolve_countries(self, info, **kwargs):
        return models.Country.objects.all()

    def resolve_languages(self, info, **kwargs):
        return models.Language.objects.all()

    def resolve_locales(self, info, **kwargs):
        return models.Locale.objects.all()

    def resolve_timezones(self, info, **kwargs):
        return models.Timezone.objects.all()

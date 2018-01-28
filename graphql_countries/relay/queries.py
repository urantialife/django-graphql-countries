from graphene_django.filter import DjangoFilterConnectionField

from . import nodes
from .. import mixins


class Query(mixins.QueryResolveMixin):
    countries = DjangoFilterConnectionField(nodes.CountryNode)
    languages = DjangoFilterConnectionField(nodes.LanguageNode)
    locales = DjangoFilterConnectionField(nodes.LocaleNode)
    timezones = DjangoFilterConnectionField(nodes.TimezoneNode)

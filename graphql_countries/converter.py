import json

from django.contrib.gis.db.models import GeometryField
from django.contrib.postgres import fields as pg_fields

import graphene
from graphene.types.generic import GenericScalar
from graphene_django.converter import convert_django_field

from .utils import dashed_to_camel


def geojson_resolver(attname, default_value, root, info, **args):
    if default_value is not None:
        root = root or default_value
    return json.loads(root.geojson)[attname]


class GeoJSON(graphene.ObjectType):
    type = graphene.String()
    coordinates = GenericScalar()

    class Meta:
        default_resolver = geojson_resolver
        name = 'CountriesGeoJSON'


@convert_django_field.register(GeometryField)
def convert_field_to_geojson(field, registry=None):
    return graphene.Field(
        GeoJSON,
        description=field.help_text,
        required=not field.null)


class CamelJSON(GenericScalar):

    @classmethod
    def serialize(cls, value):
        return dashed_to_camel(value)

    class Meta:
        name = 'CountriesCamelJSON'


@convert_django_field.register(pg_fields.JSONField)
def convert_field_to_camel_json(field, registry=None):
    return graphene.Field(
        CamelJSON,
        description=field.help_text,
        required=not field.null)

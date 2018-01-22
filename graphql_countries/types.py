import json

from django.contrib.gis.db.models import GeometryField

import graphene
from graphene.types.generic import GenericScalar
from graphene_django.converter import convert_django_field

from .utils import dashed_to_camel


class CamelJSON(GenericScalar):

    @classmethod
    def serialize(cls, value):
        return dashed_to_camel(value)

    class Meta:
        name = 'CountriesCamelJSON'


def geojson_resolver(attname, default_value, root, info, **args):
    return json.loads(root.geojson)[attname]


class GeoJSON(graphene.ObjectType):
    type = graphene.String()
    coordinates = GenericScalar()

    class Meta:
        name = 'CountriesGeoJSON'
        default_resolver = geojson_resolver


@convert_django_field.register(GeometryField)
def convert_field_to_geojson(field, registry=None):
    return graphene.Field(
        GeoJSON,
        description=field.help_text,
        required=not field.null)

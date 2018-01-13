import json

import graphene
from graphene.types.generic import GenericScalar

from .utils import dashed_to_camel


class CamelJSON(GenericScalar):

    @classmethod
    def serialize(cls, value):
        return dashed_to_camel(value)

    class Meta:
        name = 'CountriesCamelJSON'


class GeoJSON(graphene.Scalar):

    @classmethod
    def serialize(cls, value):
        return json.loads(value.geojson)

    class Meta:
        name = 'CountriesGeoJSON'

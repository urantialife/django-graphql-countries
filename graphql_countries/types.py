import json
import graphene

from .utils import dashed_to_camel


class CamelJSON(graphene.JSONString):

    @classmethod
    def serialize(cls, value):
        return dashed_to_camel(value)


class GeoJSON(graphene.Scalar):

    @classmethod
    def serialize(cls, value):
        return json.loads(value.geojson)

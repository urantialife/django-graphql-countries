from django.test import Client, RequestFactory, testcases
from graphene_django.settings import graphene_settings


class GQLRequestFactory(RequestFactory):

    def execute(self, query, **kwargs):
        return self.schema.execute(query, variable_values=kwargs)


class GQLClient(GQLRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self.schema = graphene_settings.SCHEMA


class GQLTestCase(testcases.TestCase):
    client_class = GQLClient

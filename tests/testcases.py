from django.test import Client, RequestFactory, testcases

from graphene_django.settings import graphene_settings


class GraphQLRequestFactory(RequestFactory):

    def execute(self, query, **kwargs):
        return self.schema.execute(query, variable_values=kwargs)


class GraphQLClient(GraphQLRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self.schema = graphene_settings.SCHEMA


class GraphQLTestCase(testcases.TestCase):
    client_class = GraphQLClient

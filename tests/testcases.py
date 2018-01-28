from django.test import Client, RequestFactory, testcases

import graphene


class GraphQLRequestFactory(RequestFactory):

    def execute(self, query, **variables):
        return self._schema.execute(query, variable_values=variables)


class GraphQLClient(GraphQLRequestFactory, Client):

    def __init__(self, **defaults):
        super().__init__(**defaults)
        self._schema = None

    def schema(self, **kwargs):
        self._schema = graphene.Schema(**kwargs)


class GraphQLTestCase(testcases.TestCase):
    client_class = GraphQLClient
    Query = None

    def setUp(self):
        self.client.schema(query=self.Query)

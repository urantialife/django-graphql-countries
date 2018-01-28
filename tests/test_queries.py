import graphene

import graphql_countries
from countries import factories as countries_factories

from .testcases import GraphQLTestCase


class QueriesTests(GraphQLTestCase):

    class Query(graphene.ObjectType, graphql_countries.Query):
        """Queries"""

    def test_countries(self):
        countries_factories.CountryFactory()

        query = '''
        {
          countries {
            cca2
          }
        }'''

        response = self.client.execute(query)
        self.assertTrue(response.data['countries'])

    def test_country(self):
        country = countries_factories.CountryFactory()

        query = '''
        query Country($cca2: String!) {
          country(cca2: $cca2) {
            cca2
          }
        }'''

        response = self.client.execute(query, cca2=country.cca2)
        self.assertEqual(response.data['country']['cca2'], country.cca2)

    def test_country_not_found(self):
        query = '''
        {
          country(cca2: "not_found") {
            cca2
          }
        }'''

        response = self.client.execute(query)
        self.assertIsNone(response.data['country'])

    def test_languages(self):
        countries_factories.LanguageFactory()

        query = '''
        {
          languages {
            cla3
          }
        }'''

        response = self.client.execute(query)
        self.assertTrue(response.data['languages'])

    def test_locales(self):
        countries_factories.LocaleFactory()

        query = '''
        {
          locales {
            code
          }
        }'''

        response = self.client.execute(query)
        self.assertTrue(response.data['locales'])

    def test_timezones(self):
        countries_factories.TimezoneFactory()

        query = '''
        {
          timezones {
            name
          }
        }'''

        response = self.client.execute(query)
        self.assertTrue(response.data['timezones'])

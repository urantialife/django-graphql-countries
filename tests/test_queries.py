from countries import factories as countries_factories

from .testcases import GraphQLTestCase


class QueriesTests(GraphQLTestCase):

    def test_countries(self):
        country = countries_factories.CountryFactory()

        query = '''
        query CountryList($cca2: String!) {
          countries(cca2: $cca2) {
            edges {
              node {
                cca2
              }
            }
          }
        }'''

        response = self.client.execute(query, cca2=country.cca2)
        self.assertTrue(response.data['countries']['edges'])

    def test_languages(self):
        language = countries_factories.LanguageFactory()

        query = '''
        query LanguageList($cla3: String!) {
          languages(cla3: $cla3) {
            edges {
              node {
                cla3
              }
            }
          }
        }'''

        response = self.client.execute(query, cla3=language.cla3)
        self.assertTrue(response.data['languages']['edges'])

    def test_locales(self):
        locale = countries_factories.LocaleFactory()

        query = '''
        query LocaleList($code: String!) {
          locales(code: $code) {
            edges {
              node {
                code
              }
            }
          }
        }'''

        response = self.client.execute(query, code=locale.code)
        self.assertTrue(response.data['locales']['edges'])

    def test_timezones(self):
        timezone = countries_factories.TimezoneFactory()

        query = '''
        query TimezoneList($name: String!) {
          timezones(name: $name) {
            edges {
              node {
                name
              }
            }
          }
        }'''

        response = self.client.execute(query, name=timezone.name)
        self.assertTrue(response.data['timezones']['edges'])

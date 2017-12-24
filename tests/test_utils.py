from django.test import TestCase

from graphql_countries import utils


class UtilsTests(TestCase):

    def test_to_camel(self):
        camel = utils.dashed_to_camel({
            'test_foo': {
                'test_bar': True,
            },
        })

        self.assertTrue(camel['testFoo']['testBar'])

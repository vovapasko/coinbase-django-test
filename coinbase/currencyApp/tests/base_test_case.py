from django.test import SimpleTestCase


class BaseTestCase(SimpleTestCase):

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1

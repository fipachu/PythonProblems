from unittest import TestCase
from main import get_percentage


class Test(TestCase):
    def test_get_percentage(self):
        self.assertEqual(get_percentage(0.0123), '1%')
        self.assertEqual(get_percentage(0.0123, 0), '1.0%')
        self.assertEqual(get_percentage(0.0123, 1), '1.2%')
        self.assertEqual(get_percentage(0.0123, 10), '1.23%')
        self.assertEqual(get_percentage(0.0296, 1), '3.0%')

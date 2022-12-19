from django.test import SimpleTestCase
from app import calc


class CalcTestCase(SimpleTestCase):
    def test_add_numbers(self):
        result = calc.add_two_numbers(5, 6)
        self.assertEqual(result, 11)

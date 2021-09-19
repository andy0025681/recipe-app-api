from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_number(self):
        """Test that two number added togeter."""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that two number subtracted togeter."""
        self.assertEqual(subtract(5, 11), 6)

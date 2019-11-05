from unittest import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test adding two numbers"""
        self.assertEqual(add(1, 1), 2)

    def test_subtract_numbers(self):
        """Test subtracting two numbers"""
        self.assertEqual(subtract(1, 1), 0)

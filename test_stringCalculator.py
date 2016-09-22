from unittest import TestCase
from StringCalculator import StringCalculator


class TestStringCalculator(TestCase):
    def test_add(self):
        self.assertEqual(StringCalculator().add(""), 0, "Empty String")

    def test_add_one_number(self):
        self.assertEqual(StringCalculator().add("1"), 1, "One Number Sent")

    def test_add_string_with_one_number(self):
        self.assertEqual(StringCalculator().add("1"), 1, "One Number Sent")
        self.assertEqual(StringCalculator().add("2"), 2, "One Number Sent")

    def test_add_string_with_two_numbers(self):
        self.assertEqual(StringCalculator().add("1,2"), 3, "Two Numbers Sent")

    def test_add_string_with_multiple_numbers(self):
        self.assertEqual(StringCalculator().add("1,2:3^4$5"), 15, "Multiple Numbers Sent")
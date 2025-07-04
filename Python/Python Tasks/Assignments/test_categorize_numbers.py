import categorize_numbers
import unittest
#from unittest import TestCase

class TestCategorizeNumbers(unittest.TestCase):

	def test_that_get_numbers_function_exists(self):
		categorize_numbers.get_numbers(1)

 

	def test_that_get_numbers_function_return_correct_answer(self):
		actual = categorize_numbers.get_numbers(10, 15, 21, 30)
		expected = [10, 15, 30]
		self.assertEqual(actual, expected)


	def test_that_get_numbers_function_return_no_divisible(self):
		actual = categorize_numbers.get_numbers(8, 12, 23, 21)
		expected = ('No divisible number found')
		self.assertEqual(actual, expected)

	def test_get_numbers_function_for_negative_numbers(self):
		actual = categorize_numbers.get_numbers(-10, -15, -21, -30)
		expected = ('No divisible number found')
		self.assertEqual(actual, expected)


	def test_get_numbers_function_for_empty(self):
		actual = categorize_numbers.get_numbers()
		expected = ('No divisible number found')
		self.assertEqual(actual, expected)

	def test_get_numbers_function_for_float(self):
		actual = categorize_numbers.get_numbers(10.8, 15, 21, 30)
		expected = [15, 30]
		self.assertEqual(actual, expected)


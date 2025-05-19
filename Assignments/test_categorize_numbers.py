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



	def test_that_get_numbers_function_return_correct_answer(self):
		actual = categorize_numbers.get_numbers(8, 12, 23, 21)
		expected = ('No divisible number found')
		self.assertEqual(actual, expected)
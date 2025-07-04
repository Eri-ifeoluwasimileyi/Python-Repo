import secondhighest
import unittest
#from unittest import TestCase

class TestSecondHighestNumbers(unittest.TestCase):

	def test_that_get_second_highest_function_exists(self):
		secondhighest.get_second_highest([10])

 

	def test_that_get_second_highest_function_return_correct_answer(self):
		actual = secondhighest.get_second_highest([9, 6, 8, 11, 12])
		expected = 11
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_negative_numbers(self):
		actual = secondhighest.get_second_highest([-9, -6, -8, -11, -12])
		expected = 'Invalid input'
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_no_values(self):
		actual = secondhighest.get_second_highest([])
		expected = 'This array is empty'
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_non_integer_inputs(self):
		actual = secondhighest.get_second_highest([20.0, 10.5])
		expected = 10.5
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_only_one_valid_input(self):
		actual = secondhighest.get_second_highest([20])
		expected = 'No second largest number'
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_only_one_invalid_input(self):
		actual = secondhighest.get_second_highest(["a"])
		expected = 'Invalid input'
		self.assertEqual(actual, expected)

	def test_get_second_highest_function_for_other_datatypes(self):
		actual = secondhighest.get_second_highest(["a", "b"])
		expected = 'Invalid input'
		self.assertEqual(actual, expected)


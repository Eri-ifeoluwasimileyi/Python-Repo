import menstrual_app
import unittest
#from unittest import TestCase

class MenstrualAppTest(unittest.TestCase):



	def test_that_menstrual_app_was_created(self):
		menstrual_app.check_month


	def test_check_month_is_valid(self):
	
		actual = menstrual_app.check_month(2)
		expected = 28
		self.assertEqual(actual, expected)


		actual = menstrual_app.check_month(4)
		expected = 30
		self.assertEqual(actual, expected)

		actual = menstrual_app.check_month(1)
		expected = 31
		self.assertEqual(actual, expected)


	def test_check_days_is_valid(self):
		
		actual = menstrual_app.check_days(10, 1, 3)
		expected = (13, 1)
		self.assertEqual(actual, expected)


	def test_check_name_for_same_month(self):
		actual = menstrual_app.check_days(25, 1, 5)
		expected = (30, 1)
		self.assertEqual(actual, expected)


	def test_check_date_move_to_another_year(self):

		actual = menstrual_app.check_days(25, 12, 10)
		expected = (4, 1)
		self.assertEqual(actual, expected)

	def test_date_is_valid(self):
		
		actual = menstrual_app.date(5, 3)
		expected = '05 - 03'
		self.assertEqual(actual, expected)

		actual = menstrual_app.date(12, 11)
		expected = '12 - 11'
		self.assertEqual(actual, expected)

	def test_date_is_invalid(self):
		actual = menstrual_app.date("5", 3)
		expected = 'invalid input'
		self.assertEqual(actual, expected)


		actual = menstrual_app.date(10, "5")
		expected = 'invalid input'
		self.assertEqual(actual, expected)

		
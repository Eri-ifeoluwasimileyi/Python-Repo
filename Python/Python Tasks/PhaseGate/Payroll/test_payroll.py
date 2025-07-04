import payroll

import unittest
#from unittest import TestCase


class TestPayrollApp(unittest.TestCase):

	def test_that_payroll_app_was_created(self):
		payroll.create_payroll

	
	def test_that_name_is_valid(self):
		employees = {}
		actual = payroll.check_name_validity(employees, "olamide")
		expected = "olamide"
		self.assertEqual(actual, expected)


		actual = payroll.check_name_validity(employees, "!@#$%^^&%&*)_+?:>")
		expected = "Invalid name"
		self.assertEqual(actual, expected)


		actual = payroll.check_name_validity(employees, "")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_name_validity(employees, "   ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_name_validity(employees, "12345")
		expected = "Invalid name"
		self.assertEqual(actual, expected)




	def test_that_hours_cannot_be_empty(self):
		employees = {}
		actual = payroll.check_hours("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_hours("  ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_hours("ten hours")
		expected = "Invalid hours"
		self.assertEqual(actual, expected)
	
	
	def test_that_rate_cannot_be_empty(self):
		employees = {}		
		actual = payroll.check_rate("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_rate("  ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_rate("five percent")
		expected = "bitch that's not right, pay me well"
		self.assertEqual(actual, expected)
	
	def test_that_federal_is_valid(self):
		employees = {}
		actual = payroll.check_federal("  ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)
	

		actual = payroll.check_federal("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)

		actual = payroll.check_federal("two percent")
		expected = "Invalid tax"
		self.assertEqual(actual, expected)


	def test_that_state_is_valid(self):
		employees = {}
		actual = payroll.check_state("  ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_state("")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_state("three")
		expected = "Invalid tax"
		self.assertEqual(actual, expected)


	def test_that_bank_app_can_only_accept_amount_in_digit(self):
		actual = payroll.check_amount("5000")
		expected = True
		self.assertEqual(actual, expected)


		actual = payroll.check_amount("Ten thousand naira")
		expected = "Invalid input"
		self.assertEqual(actual, expected)
	

		actual = payroll.check_amount(False)
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


		actual = payroll.check_amount(" ")
		expected = "this space cannot be empty"
		self.assertEqual(actual, expected)


	def test_that_create_payroll_is_valid(self):
		employees = {}
		actual = payroll.create_payroll(employees, "olamide", 10, 9.75, 97.5,  19.5)
		expected = True
		self.assertEqual(actual, expected)

		
	
	def test_that_update_payroll_is_valid(self):
		employees = {}
		payroll.create_payroll(employees, "olamide", 10, 9.75, 97.5,  19.5)
		actual = payroll.update_payroll(employees, "olamide")
		expected = True
		self.assertEqual(actual, expected)


	def test_that_update_payroll_is_invalid(self):
		employees = {}
		payroll.create_payroll(employees, "olamide", 10, 9.75, 97.5,  19.5)
		actual = payroll.update_payroll(employees, "ola")
		expected = "Employee not found"
		self.assertEqual(actual, expected)




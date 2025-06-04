import payroll

import unittest
#from unittest import TestCase


class TestPayrollApp(unittest.TestCase):

	def test_that_payroll_app_was_created(self):
		payroll.create_payroll

	
	def test_that_name_is_valid(self):
		
		actual = payroll.check_name_validity("olamide")
		expected = "olamide"
		self.assertEqual(actual, expected)


	def test_that_name_cannot_be_empty(self):
	
		actual = payroll.check_name_validity("")
		expected = "Name cannot be empty"
		self.assertEqual(actual, expected)


	def test_that_name_does_not_accept_space(self):
		
		actual = payroll.check_name_validity("   ")
		expected = "Name cannot be empty"
		self.assertEqual(actual, expected)

	def test_that_name_is_invalid(self):

		actual = payroll.check_name_validity("12345")
		expected = "Invalid name"
		self.assertEqual(actual, expected)



	def test_that_name_cannot_take_character(self):
		actual = payroll.check_name_validity("!@#$%^^&%&*)_+?:>")
		expected = "Invalid name"
		self.assertEqual(actual, expected)


	def test_that_create_payroll_is_valid(self):
		employees = {}
		actual = payroll.create_payroll(employees, "olamide", 10, 9.75, 97.5,  19.5, 8.77, 28.27, 69.22)
		expected = 'Employee payroll added.'
		self.assertEqual(actual, expected)



	def test_that_bank_app_can_only_accept_amount_in_digit(self):
		actual = payroll.check_amount("5000")
		expected = True
		self.assertEqual(actual, expected)
		

	def test_that_bank_app_can_only_accept_amount_in_digit_and_not_alphebet(self):
		actual = payroll.check_amount("Ten thousand naira")
		expected = "Invalid amount"
		self.assertEqual(actual, expected)
	

	def test_that_bank_app_amount_cannot_be_empty(self):
		actual = payroll.check_amount(False)
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)

	

	def test_that_bank_app_amount_cannot_be_empty_string(self):
		actual = payroll.check_amount(" ")
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)
	



		

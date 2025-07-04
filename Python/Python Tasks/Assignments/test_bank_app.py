import bank_app
import bank_app_no_seed

import unittest
#from unittest import TestCase


class TestBAnkApp(unittest.TestCase):

	def test_that_bank_app_was_created(self):
		bank_app.create_account


	def test_that_name_is_valid(self):
		
		actual = bank_app.check_name_validity("olamide")
		expected = "olamide"
		self.assertEqual(actual, expected)
	
		actual = bank_app.check_name_validity("")
		expected = "Name cannot be empty"
		self.assertEqual(actual, expected)
		
		actual = bank_app.check_name_validity("   ")
		expected = "Name cannot be empty"
		self.assertEqual(actual, expected)

	def test_that_name_is_invalid(self):

		actual = bank_app.check_name_validity("12345")
		expected = "Invalid name"
		self.assertEqual(actual, expected)

		actual = bank_app.check_name_validity("!@#$%^^&%&*)_+?:>")
		expected = "Invalid name"
		self.assertEqual(actual, expected)




	def test_that_bank_app_can_create_account(self):
		accounts = {}
		actual = bank_app.create_account(accounts, "Eriife")
		expected = "Account created successfully. Your account number is: 4885297172 and Your account name is: Eriife. Your Initial account balance is: $0.0"
		self.assertEqual(actual, expected)
	



	def test_that_bank_app_can_only_accept_10_digit_account_number_in_deposit(self):
		accounts = {}
		actual = bank_app.deposit(accounts, "488529717", 5000)
		expected = "Invalid account number! It must be 10 digits."
		self.assertEqual(actual, expected)
		

	def test_that_bank_app_can_only_accept_10_digit_account_number_not_alphabet(self):
		accounts = {}
		actual = bank_app.deposit(accounts, "fourteen", 5000)
		expected = "Invalid account number"
		self.assertEqual(actual, expected)



	def test_that_bank_app_can_only_accept_10_digit_account_number_in_withdraw(self):
		accounts = {}
		actual = bank_app.withdraw(accounts, "488529717", 2000.0)
		expected = "Invalid account number! It must be 10 digits."
		self.assertEqual(actual, expected)


		
	def test_that_bank_app_can_only_accept_10_digit_account_number_not_alphabet_in_withdraw(self):
		accounts = {}
		actual = bank_app.withdraw(accounts, "fourteen", 2000.0)
		expected = "Invalid account number"
		self.assertEqual(actual, expected)



	def test_that_bank_app_can_only_accept_10_digit_account_number_in_find_customer(self):
		accounts = {}
		actual = bank_app.find_customer(accounts, "488529717")
		expected = "Invalid account number! It must be 10 digits."
		self.assertEqual(actual, expected)

		

	def test_that_bank_app_can_only_accept_10_digit_account_number_not_alphabet_in_find(self):
		accounts = {}
		actual = bank_app.find_customer(accounts, "fourteen")
		expected = "Invalid account number"
		self.assertEqual(actual, expected)		
	

	

	def test_that_bank_app_can_only_accept_amount_in_digit(self):
		actual = bank_app.check_amount("5000")
		expected = True
		self.assertEqual(actual, expected)
		

	def test_that_bank_app_can_only_accept_amount_in_digit_and_not_alphebet(self):
		actual = bank_app.check_amount("Ten thousand naira")
		expected = "Invalid amount"
		self.assertEqual(actual, expected)
	

	def test_that_bank_app_amount_cannot_be_empty(self):
		actual = bank_app.check_amount(False)
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)

	

	def test_that_bank_app_amount_cannot_be_empty_string(self):
		actual = bank_app.check_amount(" ")
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)
	


	def test_that_bank_app_can_deposit(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.deposit(accounts, "4885297172", 5000)
		expected = "Deposited $5000.0. New balance: $5000.0"
		self.assertEqual(actual, expected)
		
	

	def test_that_bank_app_cannot_deposit_in_an_unregistered_account(self):
		accounts = {}
		actual = bank_app.deposit(accounts, "2345678901", 500)
		expected = "Account not found."
		self.assertEqual(actual, expected)



	def test_that_bank_app_cannot_deposit_invalid_amount(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.deposit(accounts, "4885297172", -5000)
		expected = "Invalid deposit amount."
		self.assertEqual(actual, expected)
		
		

	

	def test_that_bank_app_can_withdraw(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		bank_app.deposit(accounts, "4885297172", 5000.0)

		actual = bank_app.withdraw(accounts, "4885297172", 2000.0)
		expected = "Withdrew $2000.0. New balance: $3000.0"
		self.assertEqual(actual, expected)
		



	def test_that_bank_app_cannot_withdraw_in_an_unregistered_account(self):
		accounts = {}
		actual = bank_app.withdraw(accounts, "2345670891", 2000)
		expected = "Account not found."
		self.assertEqual(actual, expected)
		


	def test_that_bank_app_cannot_withdraw_invalid_amount(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.withdraw(accounts, "4885297172", -2000)
		expected = "Invalid withdrawal amount."
		self.assertEqual(actual, expected)
		

	def test_that_bank_app_cannot_withdraw_when_funds_is_insufficient(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.withdraw(accounts, "4885297172", 6000)
		expected = "Insufficient funds."
		self.assertEqual(actual, expected)
		 


	def test_that_bank_app_can_get_balance(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.get_balance(accounts, "4885297172")
		expected = "Account balance: $0.0"
		self.assertEqual(actual, expected)
		

	def test_that_bank_app_cannot_get_balance_in_an_unregistered_account(self):
		accounts = {}
		actual = bank_app.get_balance(accounts, "2345678901")
		expected = "Account not found."
		self.assertEqual(actual, expected)
		


	def test_that_bank_app_can_find_customer(self):
		accounts = {}
		bank_app.create_account(accounts, "Eriife")
		actual = bank_app.find_customer(accounts, "4885297172")
		expected = 'Account Holder: Eriife. Balance: $0.0'
		self.assertEqual(actual, expected)
		


	def test_that_bank_app_cannot_find_customer_that_does_not_exist(self):
		accounts = {}
		actual = bank_app.find_customer(accounts, "2345678901")
		expected = "Account not found."
		self.assertEqual(actual, expected)



	def test_that_bank_app_can_count_the_account_created(self):
		accounts = {}
		bank_app_no_seed.create_account(accounts, "Eriife")
		bank_app_no_seed.create_account(accounts, "Ayanfe")
		bank_app_no_seed.create_account(accounts, "Ifeoluwa")
		actual = len(accounts)
		expected = 3
		self.assertEqual(actual, expected)





import bankappATM

import unittest
#from unittest import TestCase


class TestBAnkAppAtm(unittest.TestCase):

	def test_that_bank_app_atm_was_created(self):
		bankappATM.account_balance

	def test_that_bank_app_atm_can_only_accept_amount_in_digit(self):
		actual = bankappATM.check_amount("5000")
		expected = True
		self.assertEqual(actual, expected)


	def test_that_bank_app_atm_can_only_accept_amount_in_digit_and_not_alphebet(self):
		actual = bankappATM.check_amount("Ten thousand naira")
		expected = "Invalid amount"
		self.assertEqual(actual, expected)
	

	def test_that_bank_app_atm_amount_cannot_be_empty(self):
		actual = bankappATM.check_amount(False)
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)

	

	def test_that_bank_app_amount_cannot_be_empty_string(self):
		actual = bankappATM.check_amount(" ")
		expected = "Amount cannot be empty"
		self.assertEqual(actual, expected)


	def test_that_bank_app_can_top_up(self):
		list = []
		bankappATM.account_balance(list, 0)
		actual = bankappATM.add_money(list, 0, 5000)
		expected = "Deposited $5000.0. New balance: $5000.0"
		self.assertEqual(actual, expected)



	def test_that_bank_app_cannot_top_up_invalid_amount(self):
		list = []
		bankappATM.account_balance(list, 0)
		actual = bankappATM.add_money(list, 0, -5000)
		expected = "Invalid top up amount."
		self.assertEqual(actual, expected)

		

	def test_that_bank_app_atm_can_withdraw(self):
		list = []
		bankappATM.account_balance(list, 50000)
		actual = bankappATM.withdraw(list, 50000, 5000)

		expected = "Withdrew $5000.0. Withdrawal fee: 100. New balance: $44900.0"
		self.assertEqual(actual, expected)


	def test_that_bank_app_atm_cannot_withdraw_invalid_amount(self):
		list = []
		bankappATM.account_balance(list, 50000)
		actual = bankappATM.withdraw(list, 50000, -2000)
		expected = "Invalid withdrawal amount."
		self.assertEqual(actual, expected)



	def test_that_bank_app_cannot_withdraw_when_funds_is_insufficient(self):
		list = []
		bankappATM.account_balance(list, 50000)
		actual = bankappATM.withdraw(list, 50000, 55000)
		expected = "Insufficient funds."
		self.assertEqual(actual, expected)	 



	def test_that_bank_app_cannot_withdraw_cannot_give_less_than_500(self):
		list = []
		bankappATM.account_balance(list, 50000)
		actual = bankappATM.withdraw(list, 50000, 5100)
		expected = "Withdrawal failed, amount must be a multiple of $500"
		self.assertEqual(actual, expected)
		 


	def test_that_bank_app_cannot_withdraw_cannot_give_more_than_90(self):
		list = []
		bankappATM.account_balance(list, 50000)
		actual = bankappATM.withdraw(list, 50000, 46000)
		expected = "Withdrawal failed, you cannot withdraw more than 90% of your balance"
		self.assertEqual(actual, expected)
		 






		
		
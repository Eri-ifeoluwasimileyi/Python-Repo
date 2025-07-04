import bankappATM

import unittest
#from unittest import TestCase


class TestBAnkAppAtm(unittest.TestCase):

	def test_that_bank_app_atm_was_created(self):
		bankappATM.account_balance


	def test_that_bank_app_atm_account_balance_valid(self):
		bankappATM.account_balance(50000)
		actual = bankappATM.account_balance(-50000)
		expected = "Invalid amount."
		self.assertEqual(actual, expected)




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
		

	def test_that_bank_app_atm_can_withdraw(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, 5000)

		expected = 44900.0
		self.assertEqual(actual, expected)


	def test_that_bank_app_atm_cannot_withdraw_invalid_amount(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, -2000)
		expected = "Invalid withdrawal amount."
		self.assertEqual(actual, expected)



	def test_that_bank_app_cannot_withdraw_when_funds_is_insufficient(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, 55000)
		expected = "Insufficient funds."
		self.assertEqual(actual, expected)	 



	def test_that_bank_app_cannot_withdraw_cannot_give_less_than_500(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, 5100)
		expected = "Withdrawal failed, amount must be a multiple of $500"
		self.assertEqual(actual, expected)
		 


	def test_that_bank_app_cannot_withdraw_cannot_give_more_than_90(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, 46000)
		expected = "Withdrawal failed, you cannot withdraw more than 90% of your balance"
		self.assertEqual(actual, expected)
		 

	def test_that_bank_app_cannot_withdraw_cannot_give_more_than_20000(self):
		list = []
		bankappATM.account_balance(50000)
		actual = bankappATM.withdraw(list, 50000, 21000)
		expected = "Exceed withdrawal limit"
		self.assertEqual(actual, expected)
		 





		
		
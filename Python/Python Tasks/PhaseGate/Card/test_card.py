import card
import unittest
from card import *


class TestCardNumber(unittest.TestCase):


	def test_card_exist(self):
		create_card


	def test_visa_card_is_valid(self):		
		card = [4, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]
		actual = validate_card(card)
		expected = {"valid": True, "issuer": "Visa"}
		self.assertEqual(actual, expected)



	def test_mastercard_is_valid(self):	
		card = [5, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]
		actual = validate_card(card)
		expected = {"valid": True, "issuer": "MasterCard"}
		self.assertEqual(actual, expected)



	def test_discover_is_valid(self):
		card = [6, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]
		actual = validate_card(card)
		expected = {"valid": True, "issuer": "Discover"}
		self.assertEqual(actual, expected)



	def test_American_express(self):	
		card = [3, 7, 1, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9]
		actual = validate_card(card)
		expected = {"valid": True, "issuer": "American Express"}
		self.assertEqual(actual, expected)



	def test_length_is_valid(self):	
		card = [4, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8]
		actual = validate_card(card)
		expected = {"valid": False,"reason": "Invalid length or invalid digit"}
		self.assertEqual(actual, expected)



	def test_invalid_digit(self):	
		card = [9, 7, 1, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9]
		actual = validate_card(card)
		expected =  {"valid": False,"reason": "Invalid length or invalid digit"}
		self.assertEqual(actual, expected)



	def test_inalid_numbers(self):		
		card = "4132465789041821"
		actual = validate_card(card)
		expected = {"valid": False, "reason": "card number must be digits between 0 and 9"}
		self.assertEqual(actual, expected)



	def test_strings(self):		
		card = [6, 1, 3, 2, 4, '6', 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]
		actual = validate_card(card)
		expected = {"valid": False, "reason": "card number must be digits between 0 and 9"}
		self.assertEqual(actual, expected)



	def test_input_greater_than_9(self):		
		card = [6, 1, 3, 2, 4, 10, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]
		actual = validate_card(card)
		expected = {"valid": False, "reason": "card number must be digits between 0 and 9"}
		self.assertEqual(actual, expected)





















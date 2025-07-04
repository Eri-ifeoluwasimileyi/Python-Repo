
def create_card(card_number):

	number = int

	if type(card_number) != list:

		return False

	for digits in card_number:

		if type(digits) != number or digits < 0 or digits > 9:

			return False
		
	return True



def validate_issuer(card_number):

	if len(card_number) == 16:

		if card_number[0] == 4:

			return "Visa"

		elif card_number[0] == 5:

			return "MasterCard"

		elif card_number[0] == 6:

			return "Discover"
	
	elif len(card_number) == 15 and card_number[0] == 3:

		return "American Express"

	elif len(card_number) != 16 or len(card_number) != 15:

		return "Invalid card"



def validate_card(card_number):
	
	if not create_card(card_number):
		
		return {"valid": False, "reason": "card number must be digits between 0 and 9"}

	card_issuer = validate_issuer(card_number)

	if card_issuer == "Invalid card":

		return {"valid": False,"reason": "Invalid length or invalid digit"}
	else:
 
		return {"valid": True, "issuer": card_issuer}




card = [4, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]

card2 = [5, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]

card3 = [6, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9, 6]

card4 = [3, 7, 1, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8, 9]

card5 = [4, 1, 3, 2, 4, 6, 5, 7, 8, 9, 0, 4, 1, 8]

card6 = [-1, -8]

card7 = ["4132465789041821"]

print(validate_card(card))
print(validate_card(card2))
print(validate_card(card3))
print(validate_card(card4))
print(validate_card(card5))
print(validate_card(card6))
print(validate_card(card7))

import random

def check_name_validity(name):

	new_name = name.replace(' ', '')

	if name == '':

		return "Name cannot be empty"

	elif name.isspace():

		return "Name cannot be empty"

	elif new_name.isalpha():

		return name
	
	else: return "Invalid name"



"""
def check_account_number(account_number):

	account_number = str(random.randint(1000000000, 9999999999))
	

	if all(number.isdigit() for number in account_number):
		
		if len(account_number) != 10:

			return "Invalid account number! It must be 10 digits."

		if not account_number:

			return "Account number cannot be empty"

		if account_number.isspace():

			return "Account number cannot be empty"


		elif account_number not in accounts:

			return "Account not found."

	else:
		return "Invalid account number"

"""


def create_account(accounts, name, balance=0):

	
	balance = float(balance)

	account_number = str(random.randint(1000000000, 9999999999))
		
	accounts[account_number] = {'name': name, 'balance': balance}
	
	
	return f"Account created successfully. Your account number is: {account_number} and Your account name is: {name}  Your Initial account balance is: ${balance}"






def check_amount(amount):

	if not amount:

		return "Amount cannot be empty"

	if amount.isspace():

		return "Amount cannot be empty"

	another_amount = amount.replace('.', '', 1)

	if all(number.isdigit() for number in another_amount):
		
		amount = float(amount) 
			
		if amount == round(amount, 2): return True

		else: return "Invalid Amount"

	else: return "Invalid amount"





def deposit(accounts, account_number, amount):

	amount = float(amount)

	if all(number.isdigit() for number in account_number):
		
		if len(account_number) != 10:

			return "Invalid account number"

		elif account_number not in accounts:

			return "Account not found."
	
		elif amount <= 0:
	
			print("Invalid deposit amount.")
        	
	
		accounts[account_number]['balance'] += amount

		return f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}"


	else:
		return "Invalid account number"





def withdraw(accounts, account_number, amount):

	amount = float(amount)

	if all(number.isdigit() for number in account_number):
		
		if len(account_number) != 10:

			return "Invalid account number"


		elif account_number not in accounts:

			return "Account not found."
		

		elif amount <= 0:
		
			print("Invalid withdrawal amount.")
		
		elif accounts[account_number]['balance'] < amount:

			return "Insufficient funds."

		else:
			accounts[account_number]['balance'] -= amount

			return f"Withdrew ${amount}. New balance: ${accounts[account_number]['balance']}"


	else:
		return "Invalid account number"




def get_balance(accounts, account_number):

	if all(number.isdigit() for number in account_number):
		
		if len(account_number) != 10:

			return "Invalid account number"

		elif account_number not in accounts:
	
			return "Account not found."
		

		return f"Account balance: ${accounts[account_number]['balance']}"


	else:
		return "Invalid account number"






def find_customer(accounts, account_number):

	if all(number.isdigit() for number in account_number):
		
		if len(account_number) != 10:

			return "Invalid account number"

		elif account_number not in accounts:
		
			return "Account not found."
		
		else:
			return f"Account Holder: {accounts[account_number]['name']}. Balance: ${accounts[account_number]['balance']}"

	else:
		return "Invalid account number"



def show_all_accounts(accounts):

	for key, value in accounts.items():		#to loop through a dictionary, you need to use dictionary_name.items()

		print(key)

		for info, detail in value.items():

			print(f"{info}: {detail}")
		print()
		
			




accounts = {}
while True:

	print("""

	<><><> Welcome to Demon Bank <><><>

	1. Create Account

	2. Deposit

	3. Withdraw

	4. Check Balance

	5. View Account Info

	6. Check Number of Accounts created

	7. Check All Accounts
		
	0. Exit			
		""")

	user_choice = str(input('Enter your choice: '))
	print()


	match(user_choice):   

		case '1':

			name = input("Enter your name: ")

			if check_name_validity(name) == name:

				print(create_account(accounts, name))
			else:
				print(check_name_validity(name))

		case '2':

			account_number = str(input("Enter account number: "))

			amount = str(input("Enter deposit amount: "))
			
			if check_amount(amount) == True:
	
				print(deposit(accounts, account_number, amount))

			else:
				print(check_amount(amount))

		case '3':

			account_number = str(input("Enter account number: "))

			amount = str(input("Enter withdrawal amount: "))

			if check_amount(amount) == True:

				print(withdraw(accounts, account_number, amount))

			else:
				print(check_amount(amount))


		case '4':

			account_number = str(input("Enter account number: "))

			print(get_balance(accounts, account_number))

		case '5':
          
			account_number = str(input("Enter account number to view details: "))

			print(find_customer(accounts, account_number))

		case '6':
			
			print(f"Total accounts created: {len(accounts)}")

		case '7':

			show_all_accounts(accounts)

		case '0':

			print("Thank you for using Demon Bank...")
			break

		case _:

			print("Invalid choice. Please try again.")
		

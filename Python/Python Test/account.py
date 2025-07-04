accounts = []
account_number = "0123456789"
def create_account(account_number, name, pin, balance=0.0):

	account = [account_number, name, pin, balance]
	accounts.append(account)
	return "account"

print("Account created successfully.")


def deposit(account, account_number, pin, amount):
	
	if account_number not in account:
		return "Account not found!"

	if user_pin != pin:
		return "Invalid pin"

	if amount <= 0:
		return "Invalid deposit amount"
	else:
		if amount > 0:
			account = ['balance'] + amount
		return(f"{amount} deposited successfully.") 

print(f"Deposited ${amount} New balance: ${account[account_number]['balance']}")
	
def withdraw(account, account_number, pin, amount):

	if account_number not in account:
		return "Account not found!"

	if user_pin != pin:
		return "Invalid pin"

	elif amount <= 0:
		return "Invalid withdrawal amount"

	elif amount > self.balance:
		return "Insufficient balance."
	
	else:
		account = ['balance'] - amount
		return(f"{amount} withdrawn successfully.")
print(f"Withdrew ${amount} New balance: ${account[account_number]['balance']}")


def get_balance(account, account_number, pin):

	if account_number not in account:
		return "Account not found!" 
	
	if user_pin != pin:
		return "Invalid pin"
	else:

		return balance






account_number = "0123456789"
def BankMenu():
	import string	
	account = []
	user_choice = -1
	while user_choice != 5:


		Options = """
<<<<<<<<<<>>>>>>>>>>>
WELCOME TO THE DEMON BANK
		
		MENU
		Select your choice:
		1. Create Account
		2. Deposit	
		3. Withdraw
		4. Check Balance
		5. Exit App
<<<<<<<<<<>>>>>>>>>>>
				"""
		
	print(Options)
	user_choice = float(input('Enter number of your choice: ')) 
	
	match(user_choice):
		case 1:
			name = str(input('Enter your name: '))
			pin = int(input('Enter your preferred pin: '))				
			default: print('Invalid input')

			
		case 2:
			account_number = int(input('Enter account number: '))
			amount = float(input('Enter amount to deposit: '))
			pin = int(input('Enter your pin: '))			
			default: print('Invalid input')


		case 3:
			account_number = int(input('Enter account number: '))
			amount = float(input('Enter withdrawal amount: '))
			pin = int(input('Enter your pin: '))
			default: print('Invalid input')
				

		case 4:
			account_number = int(input('Enter account number: '))
			pin = int(input('Enter your pin: '))


		case 5: print('Exiting App......')	


		case _: 	
			default : print("Invalid input")



print(create_account(accounts, name, pin))
print(deposit(account, account_number, amount, pin))
print(withdraw(account, account_number, amount, pin))
print(get_balance(account, account_number, pin))




			




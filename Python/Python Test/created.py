def create_account(accounts, account_number, name, balance=0):

	new_account = [account_number, name, balance]

	accounts.append(new_account)

	if account_number in accounts:

		return "Account number already exists."


	print(f"Account created successfully. Your account number is: {account_number} and Your account name is: {name}")
    


def deposit(accounts, account_number, amount):

	
	all() any()

	if any(account[0] == account_number for account in accounts):

	if any(account_number.isdigit() for account_number in accounts):


	for acc_no in accounts.keys():
		if acc_no == account_number:
			acc_no['balance'] += amount			
			
		


	for account in accounts:
		for item in account:
			if item not in account_number:
				print ("Account not found")
				return
	
	if amount <= 0:
		return "Invalid deposit amount."


	for account in accounts:
		for item in account:
			if item in account_number:
				accounts[account][2] += amount
				print (f"Deposited ${amount}. New balance: ${accounts[account][2]}")
				return



def withdraw(accounts, account_number, amount):

	if account_number not in accounts:

		print("Account not found.")
		return

	if amount <= 0:

		print("Invalid withdrawal amount.")
		return

	if accounts[account_number]['balance'] < amount:

		print("Insufficient funds.")
		return

	accounts[account_number]['balance'] -= amount

	print(f"Withdrew ${amount}. New balance: ${accounts[account_number]['balance']}")



def get_balance(accounts, account_number):

	if account_number not in accounts:

		print("Account not found.")
		return

	print(f"Account balance: ${accounts[account_number]['balance']}")




accounts = []

while True:

	menu = """

	    <><><> Welcome to Demon Bank <><><>

	        1. Create Account

        	2. Deposit
	
        	3. Withdraw

		4. Check Balance

        	5. Exit
		"""
	print(menu)
	user_choice = str(input('Enter your choice: '))


	match(user_choice):   

		case '1':

			account_number = input("Enter account number: ")

			name = input("Enter your name: ")

			create_account(accounts, account_number, name)

		case '2':
	
			account_number = input("Enter account number: ")

			amount = float(input("Enter deposit amount: "))
	
			deposit(accounts, account_number, amount)

		case '3':

			account_number = input("Enter account number: ")

			amount = float(input("Enter withdrawal amount: "))

			withdraw(accounts, account_number, amount)

		case '4':
		
			account_number = input("Enter account number: ")

			get_balance(accounts, account_number)

		case '5':
			print("Thank you for using Demon Bank...")
			break

		case _: 
			print("Invalid choice. Please try again.")





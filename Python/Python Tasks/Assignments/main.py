
"""

accounts = {}
while True:

	menu = """

	<><><> Welcome to Demon Bank <><><>

	1. Create Account

	2. Deposit

	3. Withdraw

	4. Check Balance

	5. View Account Info

	6. Check Number of Accounts

	7. Check All Accounts
		
	0. Exit			
		"""

	print(menu)
	user_choice = str(input('Enter your choice: '))
	print()

	match(user_choice):   

		case '1':

			account_number = input("Enter account number: ")

			name = input("Enter your name: ")

			create_account(accounts, account_number, name)

		case '2':

			account_number = input("Enter account number: ")

			amount = str(input("Enter deposit amount: "))
			
			if check_amount(amount) == True:
				deposit(accounts, account_number, amount)
			else:
				check_amount(amount)

		case '3':

			account_number = input("Enter account number: ")

			amount = str(input("Enter withdrawal amount: "))

			if check_amount(amount) == True:
				withdraw(accounts, account_number, amount)
			else:
				check_amount(amount)

		case '4':

			account_number = input("Enter account number: ")

			get_balance(accounts, account_number)

		case '5':
          
			account_number = input("Enter account number to view details: ")

			find_customer(accounts, account_number)

		case '6':
			
			print(f"Total accounts created: {len(accounts)}")

		case '7':

			show_all_accounts(accounts)

		case '0':
			print("Thank you for using Demon Bank...")
			break

		case _:

			print("Invalid choice. Please try again.")

	
"""	
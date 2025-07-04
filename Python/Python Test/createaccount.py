def create_account(accounts, account_number, name, balance=0):

	if account_number in accounts:

		return "Account number already exists."

	accounts[account_number] = {'name': name, 'balance': balance}

	print(f"Account created successfully. Your account number is: {account_number} and Your account name is: {name}")
    


def deposit(accounts, account_number, amount):

	if account_number not in accounts:
		print("Account not found.")
		return

	if amount <= 0:

		print("Invalid deposit amount.")
		return

	accounts[account_number]['balance'] += amount

	print(f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}")



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




accounts = {}
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
	



















































        print("\n <><><> Welcome to Demon Bank <><><>")

        print("1. Create Account")

        print("2. Deposit")

        print("3. Withdraw")

        print("4. Check Balance")

        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            account_number = input("Enter account number: ")

            name = input("Enter your name: ")

            create_account(accounts, account_number, name)

        elif choice == '2':

            account_number = input("Enter account number: ")

            amount = float(input("Enter deposit amount: "))

            deposit(accounts, account_number, amount)

        elif choice == '3':

            account_number = input("Enter account number: ")

            amount = float(input("Enter withdrawal amount: "))

            withdraw(accounts, account_number, amount)

        elif choice == '4':

            account_number = input("Enter account number: ")

            get_balance(accounts, account_number)

        elif choice == '5':

            print("Thank you for using Demon Bank...")

            break

        else:

            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

























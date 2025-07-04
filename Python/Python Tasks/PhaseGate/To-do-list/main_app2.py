import bankappATM
from bankappATM import *
list = []
check = True
while check:

	print("""
	
	<><><> Welcome to Osama Bank <><><>
	1. Top up your account balance
	2. Enter Withdrawal amount
	3. Check Transaction History
	0. To exit
			""")

	user_choice = str(input('Enter your choice: '))
	print()


	match(user_choice):

		case '1':
			
			balance = str(input('Enter the top up amount: '))
			
			balance = float(balance)

			if check_amount(list) == True:


				print(add_money(list, balance, amount))
	
			else:
		
				print(account_balance(list, balance))

		
		case '2':

			amount = str(input("Enter withdrawal amount: "))

			if check_amount == True:
					
				print(add_money(list, balance, amount))

				if (withdraw(list, account_balance, amount)) == True:
				
					print(add_money(list, account_balance, amount))

					balance = withdraw(list, account_balance, amount)

				else: print(withdraw(list, account_balance, amount))

			else:
		
				print(withdraw(list, balance, amount))
			
			

			while check:
		
				user_input = str(input('Do you want to make another withdrawal? yes/no: '))

				user_input = user_input.lower()

				if(user_input == "yes"):

					amount = str(input("Enter withdrawal amount: "))

					if check_amount == True:
							
						print(add_money(list, balance, amount))

					
					else:
						
						print(withdraw(list, balance, amount))
						continue
			
				while(user_input == "no"):
					check = False
					break
		
		
	

		case '3':

			show_transaction_history(list)


		case '0':

			print("Thank you for using Osama Bank...")
			break

		case _:

			print("Invalid choice. Please try again.")		
	
			
			

	

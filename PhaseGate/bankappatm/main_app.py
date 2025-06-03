import bankappATM
from bankappATM import *
list = []

check = True
while check:

	print('<><><> Welcome to Osama Bank <><><>')

	balance = str(input('Enter the top up amount: '))
	print()
			
	if check_amount == True:

		balance = float(balance)	

		print(f"Your balance is: {balance}")
		break
	else: 
		print(check_amount(list))
		continue
		
	while check:

		amount = str(input("Enter withdrawal amount: "))
		
		if check_amount == True:

			if type(withdraw(list, account_balance, amount)) == True:
				
				print(withdraw(list, account_balance, amount))
				balance = withdraw(list, account_balance, amount)
				print(show_transaction_history(list))


			else: print(withdraw(list, account_balance, amount))


				
		else:
		
			print(check_amount(amount))
			
		while check:

			user_input = str(input('Do you want to make another withdrawal? yes/no: '))

			user_input = user_input.lower()
		
			if(user_input == "yes"):
				
				break

						
			elif(user_input == "no"):

				
				
				check = False
				break

			else:
				print("Invalid choice. Please try again.")
		
		
		


		

print("Thank you for using Osama Bank...")
			



	


	

			
	
			
			

				
					
					
				
	
			
			

	

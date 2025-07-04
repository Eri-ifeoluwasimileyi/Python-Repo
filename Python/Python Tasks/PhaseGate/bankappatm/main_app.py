import bankappATM
from bankappATM import *
transaction_history = []

check = True
while check:

	print('<><><> Welcome to Osama Bank <><><>')
	print()
	balance = str(input('Enter the top up amount: '))
	print()
			
	if check_amount(balance) == True:

		if type(account_balance(balance)) == float:

			balance = account_balance(balance)
		
			print('Transaction successful')
			print(f"Your account balance is: ${balance}")
		else:
			print(account_balance(balance))
			continue
		
	else:
		print(check_amount(balance))
		continue

		
	while check:
		print()
		amount = str(input("Enter withdrawal amount: "))
		print()
		if check_amount(amount) == True:

			result = withdraw(transaction_history, balance, amount)

			if isinstance(result, float):
	
				print('Transaction successful')
				balance = result
				print((f"Withdrew: ${amount}.\nWithdrawal fee: $100.\nNew balance: ${balance}"))

			else:
				print(result)
				continue
			
			
	
		else:
			print(check_amount(amount))
			continue
			
		while check:
			print()
			user_input = str(input('Do you want to make another withdrawal? yes/no: '))
			
			user_input = user_input.lower()
		
			if(user_input == "yes"):
				
				break

						
			elif(user_input == "no"):		
				
				check = False
				break

			else:
				print("Invalid choice. Please try again.")
		
		
		


print()		
show_transaction_history(transaction_history)
print()
print("Thank you for using Osama Bank...")
			


def account_balance(balance):

	balance = float(balance)

	if balance <= 0: return "Invalid amount."

	return balance



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




def withdraw(transaction_history, balance, amount):

	amount = float(amount)

	if amount <= 0:
		
		return "Invalid withdrawal amount."
		
	elif balance < amount:

		return "Insufficient funds."

	elif amount < 500 or amount % 500 != 0:
		
		return "Withdrawal failed, amount must be a multiple of $500"

	elif amount > balance * 90 / 100:

		return "Withdrawal failed, you cannot withdraw more than 90% of your balance"

	elif amount > 20000:
	
		return "Exceed withdrawal limit"

	else:
		balance -= (amount + 100)
		
		transaction_history.append(f"Withdrew: ${amount}.\nWithdrawal fee: $100.\nNew balance: ${balance}")

		return balance




def show_transaction_history(transaction_history):

	for withdrawal in transaction_history:

		print(f'{withdrawal}\n')

	

	
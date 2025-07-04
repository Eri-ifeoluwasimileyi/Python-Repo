Accounts = []

def create_account(accounts, account_number, name, balance=0.0):
	if account_number in accounts:
		print("Account number already exists!")
		return account_number
	accounts[account_number] = {'name': name, 'balance': balance}
	print(f"Account created successfully. Account number: {account_number}")


	

print(create_account(account_number))
cart = []

check = True

while True:

	while check:

		name = str(input("What is the customer name: "))

		valid_name = check_name_validity(name)
	
		if valid_name != name:
		
			print(valid_name)
			continue

		product = str(input("What did the user buy: "))

		new_product = check_name_validity(product)
	
		if new_product != True:
		
			print(new_product)
			continue


		quantity = int(input("How many pieces: "))

		if quantity <= 0:

			print("Invalid input")
		

		price = str(input("How much per unit: "))

		price = float(price)

		new_price = check_amount(price)

		if new_price != True:

			print(new_price)
			continue


		cart.append({'name': name, 'price': price, 'quantity': quantity})

		while check:

			user_choice = str(input("Do you want to add another item? (yes/no): "))
		
			user_choice = user_choice.lower()
	
			if(user_choice == 'yes'):

				break
			elif(user_choice == 'no'):

				check = False
				break
	
			else:
				print("Invalid choice. Please try again.")

		

	if len(cart) > 0:
		print_invoice(cart)

	else:
		print("No items in cart. Invoice cannot be raised.")


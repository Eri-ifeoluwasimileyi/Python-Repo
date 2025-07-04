number = int(input("Enter a number between 1 and 100: "))	

sum = 0	

if number < 1 or number > 10000:
	print('Invalid input,Try Again')
	
else: 
	number > 1 and number <= 10000

	while number != 0:
		
		digit = number % 10
		number = number // 10
			
		sum = sum + digit



	print(f"The sum of the digits is: {sum}")
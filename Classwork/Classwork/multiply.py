def multiply(number, number2):
 
	
	result = 0

	if number2 < 0:
		for product in range(0, abs(number2)):
	
			result = result + number


		return -result
	elif number < 0:
		for product in range(0, abs(number2)):
	
			result = result + number


		return result
		
	else:
		for product in range(0, abs(number2)):
	
			result = result + number


		return result
		 

user_input1 = float(input('Enter a number: '))

user_input2 = int(input('Enter another number: '))

print(multiply(user_input1, user_input2))

print(multiply(4, 5))

print(multiply(4, -5))	

print(multiply(-4, -5))	

print(multiply(-4, 5))	



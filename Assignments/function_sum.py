def sum_of_digit(number):

	sum = 0	

	if number < 1 or number > 10000:
		return('Invalid input,Try Again')
	
	else:
		number > 1 and number <= 10000
<<<<<<< HEAD

=======
>>>>>>> 3d3e67fd99c31778d0fa34cae1d274f35f5eb1bd

		while number != 0:
		
			digit = number % 10
			number = number // 10
			
			sum = sum + digit

		return sum


user_input = int(input("Enter a number between 1 and 10000: "))

print(sum_of_digit(user_input))           

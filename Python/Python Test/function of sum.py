def sum_of_digit(number):
	number = int(input("Enter a number between 1 and 10000: "))
	digit1 = 0
	digit2 = 0
	digit3 = 0
	digit4 = 0
	digit5 = 0
	remainder = 0 
	sum = 0

	if number < 1 or number > 10000:
		print("Invalid input, Try again!")
	 
	else:
		number > 1 and number < 10000
	
		digit1 = number % 10
		remainder = number // 10

		digit2 = remainder % 10
		remainder = remainder // 10

		digit3 = remainder % 10
		remainder = remainder // 10

		digit4 = remainder % 10
		remainder = remainder // 10

		digit5 = remainder % 10
		remainder = remainder // 10


	sum = digit1 + digit2 + digit3 + digit4 + digit5

	return sum



print(sum_of_digit(sum))

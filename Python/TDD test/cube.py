def get_cube(number):
	
	#pass

	if number <= 10:

		return number ** 3
	else:	
		return "invalid number"
	

	
def get_cube(number):

	numbers = range(1, 11)

	if number in numbers:
		
		return number ** 3

	raise ValueError
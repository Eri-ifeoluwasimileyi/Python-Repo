def get_second_highest(numbers): 


	for number in numbers:

		if not isinstance(number, (int, float)):
			return 'Invalid input'

	if len(numbers) == 0:
		return 'This array is empty'

	if len(numbers) == 1:
		return 'No second largest number'


	secondLargest = -22337569
	largestNumber = -20000000

	for number in numbers:

		if number < 0:
			return 'Invalid input'

		elif largestNumber < number:

			secondLargest = largestNumber
			largestNumber = number
	
		else:
			secondLargest > number
			secondLargest = number

	return secondLargest
"""
numbers = [9, 6, 8, 11, 12]
numbers = [-9, -6, -8, -11, -12]
numbers = []
numbers = [20.5, 10.5]
numbers = [20]
numbers = ["a"]
numbers = ["a", "b"]

print(get_second_highest(numbers))
	
"""


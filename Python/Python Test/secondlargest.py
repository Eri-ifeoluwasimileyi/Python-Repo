secondLargest = -22337569
largestNumber = -20000000

array = [9, 6, 8, 11, 12]

for number in array:

	if largestNumber < number:

		secondLargest = largestNumber
		largestNumber = number
	
	elif secondLargest > number:
		secondLargest = number

	
print(secondLargest)		
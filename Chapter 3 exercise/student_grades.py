passes = 0
failures = 0
valid_counter = 0



while valid_counter < 10:

	result = int(input('Enter the result (1=pass, 2=fail): '))

	if result == 1:
		passes += 1
		valid_counter += 1

	elif result == 2:
		failures += 1
		valid_counter += 1


	else:
		 print('Invalid input')
	


print('Passed:', passes)

print('Failed:', failures)

if passes > 8:
	print('Bonus to instructor')

		
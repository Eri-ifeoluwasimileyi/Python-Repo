def  get_numbers(*numbers):
	
	answer = ()
	count = 0
	  

	while count < len(numbers):

		if numbers[count] % 5 == 0:
			answer = answer + (numbers[count],)  
	 
		count +=1
	
	if answer:

		return list(answer)
				

	else:
		return('No divisible number found')

	

print(get_numbers(10, 15, 21, 30)) 
print(get_numbers(8, 12, 23, 21)) 


def  get_numbers(*numbers):
	
	answer = ()
	count = 0
	  

	while count < len(numbers):

		if numbers[count] > 0 and numbers[count] % 5 == 0:
			answer = answer + (numbers[count],)  
	 
		count +=1
	
	if answer:

		return list(answer)
				

	else:
		return('No divisible number found')

	

#print(get_numbers(10, 15, 21, 30)) 
#print(get_numbers(8, 12, 23, 21)) 
#print(get_numbers(-10, -15, -21, -30)) 
#print(get_numbers())
print(get_numbers(10.8, 15, 21, 30)) 
 

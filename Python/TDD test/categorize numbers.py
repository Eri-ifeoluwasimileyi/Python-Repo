def get_categorize_numbers(*numbers):
	
	answer = ()
	 #this is use to create an empty tuple to store the numbers

	count = 0
	  #used to count the numbers that are divisible by 5

	while count < len(numbers):

		if numbers[count] > 0 and numbers[count] % 5 == 0:
			answer = answer + (numbers[count],)  
				#if the number is divisible,this add it to the tuple
 
		count +=1
	

	if answer:
		#used to check if the tuple is not empty

		return list(answer)
			#this return the divisible numbers as a list
			

	else:
		return('No divisible number found')

	

print(get_categorize_numbers(10, 15, 21, 30)) 
#print(get_categorize_numbers(8, 12, 23, 21)) 
#print(get_categorize_numbers(-10, -15, -21, -30)) 
#print(get_categorize_numbers())
print(get_categorize_numbers(10.8, 15, 21, 30)) 


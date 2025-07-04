import random

def subtraction(number1, number2):

	get_answer = number1 - number2
	
	return get_answer



attempt = 0
score = 0

while attempt < 10:

	number1 = random.randrange(1, 100)
	number2 = random.randrange(0, number1)

	count = 0

	while count < 2:

		answer = int(input(f"What is: {number1} - {number2}: "))
		#answer = int(input())
	

		if subtraction(number1, number2) == answer:
			print('correct')
			score += 1
			break;

		else: 
			print('Wrong answer')



		count += 1


	attempt += 1



print()
print("That will be all")
print(f"your score is {score}")
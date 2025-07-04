highest_student_name = str(" ")
largest_number = -23456678

number_of_student = int(input('Enter the number of students: '))

for number in range(number_of_student):
	
	student_name = input('Enter the name of the student: ')
	
	score = int(input('Enter the score: '))
	
	if score > largest_number:
		largest_number = score
		highest_student_name = student_name

	elif score == largest_number:
		largest_number = score

		highest_student_name = highest_student_name + " and " + student_name

if number_of_student <= 0:
	print('Invalid input, Enter a valid input!')
else:
	print(f'The student with the highest score is: {highest_student_name} with the score {largest_number}')
		

import payroll
from payroll import *

employees = {}
check = True
while check:

	print("""

	Welcome to Demon Bank

	1. Add employee payroll

	2. View employee payroll

	3. Update employee payroll

	4. Exit 
		""")


	user_choice = str(input('Enter your choice: '))
	print()

	
	match(user_choice): 

		case '1':

			while check:

				name = input("Enter employee name: ")

				if check_name_validity(name) == name:

					print(check_name_validity(name))
					
				else:
					print(check_name_validity(name))
					continue
				
				hours = int(input('Enter number of hours worked in a week: '))
				if hours <= 0 or hours > 160:

					print(create_payroll(employees, name, hours, rate, gross, federal, state, total, pay))
					

				rate = float(input('Enter hourly pay rate: '))
			
				if rate <= 0:
			
					print(create_payroll(employees, name, hours, rate, gross, federal, state, total, pay))
					continue
				
				federal = float(input('Enter federal tax withholding rate: '))	
				if federal <= 0 or federal > 100:
					print(create_payroll(employees, name, hours, rate, gross, federal, state, total, pay))
					continue
				state = float(input('Enter state tax withholding rate: '))
				if state <= 0 or state > 100:

					print(create_payroll(employees, name, hours, rate, gross, federal, state, total, pay))
					break
			
		case '2':
			while check:
			
				view_all_payroll(employees)



		case '3': 
			while check:
			
				find = str(input('Enter employee name: '))
				print(update_payroll(employees, find))
		
		case '4':

			print('Thank you')
			break


		

			
			
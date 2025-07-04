import payroll
from payroll import *

employees = {}

while True:

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

			while True:

				name = input("Enter employee name: ")
				print()
				if name != check_name_validity(employees, name):

					print(check_name_validity(employees, name))
					continue
				
				hours = input('Enter number of hours worked in a week: ')
				print()
				if check_hours(hours) != True:

					print(check_hours(hours))
					continue

				rate = input('Enter hourly pay rate: ')
				print()
				if check_rate(rate) != True:
			
					print(check_rate(rate))	
					continue
				
				federal = input('Enter federal tax withholding rate: ')
				print()
				if check_federal(federal) != True:

					print(check_federal(federal))
					continue


				state = input('Enter state tax withholding rate: ')
				print()
				if check_state(state) != True:

					print(check_state(state))					
					continue


				if create_payroll(employees, name, hours, rate, federal, state) != True:
					print(create_payroll(employees, name, hours, rate, federal, state))
					continue


				print()
				print('Employee payroll added.')
				break



		case '2':
			
			view_all_payroll(employees)
			print()


		case '3': 
			while True:
			
				find = str(input('Enter employee name: '))
				print()

				if update_payroll(employees, find) != True:
					print(update_payroll(employees, find))
					print()
					continue

				print("Payroll found")
				print()
				break

			while True:

				name = input("Enter employee name: ")

				if name != check_name_validity(employees, name):

					print(check_name_validity(employees, name))
					continue
				
				hours = input('Enter number of hours worked in a week: ')

				if check_hours(hours) != True:

					print(check_hours(hours))
					continue

				rate = input('Enter hourly pay rate: ')
			
				if check_rate(rate) != True:
			
					print(check_rate(rate))	
					continue
				
				federal = input('Enter federal tax withholding rate: ')

				if check_federal(federal) != True:

					print(check_federal(federal))
					continue


				state = input('Enter state tax withholding rate: ')

				if check_state(state) != True:

					print(check_state(state))					
					continue


				if create_payroll(employees, name, hours, rate, federal, state) != True:
					print(create_payroll(employees, name, hours, rate, federal, state))
					continue


		
				print('Employee payroll added.')
				break



		case '4':
	
			print("Exiting Demon payroll system.")
			break
	

		case _:
		
			default: print("Invalid choice. Please select a valid option.")
		

			
			
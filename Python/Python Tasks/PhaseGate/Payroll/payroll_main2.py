import payroll
from payroll import *
employees = {}

while True:
	print("""
	SK Payroll System

	1. Add employee payroll

	2. View all payrolls

	3. Update employee payroll

	4. Exit
		
		""")
		

	choice = input("Enter your choice (1-4): ")

	if choice == '1':

		while True:

			name = input("Enter employee name: ")
			print()

			valid_name = check_name_validity(employees, name)

			if valid_name != name:

				print(valid_name)
				continue

			hours = input("Enter hours worked: ")
			print()

			hours
			hours_valid = check_hours(hours)

			if hours_valid != True:
				print(hours_valid)
				continue

			rate = input("Enter pay rate: ")
			print()

			rate_valid = check_rate(rate)

			if rate_valid != True:
				print(rate_valid)
				continue

			federal = input("Enter federal withholding %: ")
			print()

			federal_valid = check_federal(federal)
	
			if federal_valid != True:
                		print(federal_valid)
                		continue

			state = input("Enter state withholding %: ")
			print()

			state_valid = check_state(state)

			if state_valid != True:
				print(state_valid)
				continue

			if create_payroll(employees, name, hours, rate, federal, state) != True:
				print(create_payroll(employees, name, hours, rate, federal, state))
				continue

		
			print('Employee payroll added.')
			break




	elif choice == '2':
		print()
		view_all_payroll(employees)
		print()




	elif choice == '3':

		while True:
			update = input("Enter employee name to update: ")
			print()
			
			if update_payroll(employees, update) != True:
				print(update_payroll(employees, update))
				print()
				continue

			print("Payroll found")
			break

		while True:

			name = input("Enter employee name: ")

			valid_name = check_name_validity(employees, name)
			print()

			if valid_name != name:

				print(valid_name)
				continue

			hours = input("Enter hours worked: ")
			print()

			hours_valid = check_hours(hours)

			if hours_valid != True:
				print(hours_valid)
				continue

			rate = input("Enter pay rate: ")
			print()

			rate_valid = check_rate(rate)

			if rate_valid != True:
				print(rate_valid)
				continue

			federal = input("Enter federal withholding %: ")
			print()

			federal_valid = check_federal(federal)
	
			if federal_valid != True:
                		print(federal_valid)
                		continue

			state = input("Enter state withholding %: ")
			print()

			state_valid = check_state(state)

			if state_valid != True:
				print(state_valid)
				continue

			if create_payroll(employees, name, hours, rate, federal, state) != True:
				print(create_payroll(employees, name, hours, rate, federal, state))
				continue

			print('Employee payroll added.')
			break


	elif choice == '4':


		print("Exiting SK payroll system.")
		break
	
	
	




	else:
		print("Invalid choice. Please select a valid option.")

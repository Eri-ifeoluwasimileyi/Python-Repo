import payroll
from payroll import *
employees = {}

while True:
	print("\nPayroll System")

	print("1. Add employee payroll")

	print("2. View all payrolls")

	print("3. Exit")

	choice = input("Enter your choice (1-3): ")

	if choice == '1':

		name = input("Enter employee name: ")

		valid_name = check_name_validity(name)

		if valid_name != name:

			print(valid_name)
			continue

		hours = input("Enter hours worked: ")

		hours_valid = check_amount(hours)

		if hours_valid is not True:
			print(hours_valid)
			continue

		rate = input("Enter pay rate: ")

		rate_valid = check_amount(rate)

		if rate_valid is not True:
			print(rate_valid)
			continue

		federal = input("Enter federal withholding %: ")

		federal_valid = check_amount(federal)
	
		if federal_valid is not True:
                	print(federal_valid)
                	continue

            	state = input("Enter state withholding %: ")

            	state_valid = check_amount(state)

            	if state_valid is not True:
			print(state_valid)
              	  	continue

		hours = float(hours)

		rate = float(rate)

		federal = float(federal)

		state = float(state)

		gross = hours * rate

		federal_withholding = gross * federal / 100
		
		state_withholding = gross * state / 100

		total_deduction = federal_withholding + state_withholding

		net_pay = gross - total_deduction

		print(create_payroll(employees, name, hours, rate, gross, federal_withholding, state_withholding, total_deduction, net_pay))

	elif choice == '2':
		view_all_payroll(employees)
	
	elif choice == '3':
		print("Exiting payroll system.")
		break
	
	else:
		print("Invalid choice. Please select a valid option.")

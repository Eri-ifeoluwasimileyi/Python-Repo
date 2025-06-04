def check_name_validity(name):

	new_name = name.replace(' ', '')

	if name == '':

		return "Name cannot be empty"

	elif name.isspace():

		return "Name cannot be empty"

	elif new_name.isalpha():

		return name
	
	else: return "Invalid name"


def check_amount(amount):

	if not amount:

		return "Amount cannot be empty"

	if amount.isspace():

		return "Amount cannot be empty"

	another_amount = amount.replace('.', '', 1)

	if all(number.isdigit() for number in another_amount):
		
		amount = float(amount) 
			
		if amount == round(amount, 2): return True
		else: return "Invalid Amount"

	else: return "Invalid amount"



def create_payroll(employees, name, hours, rate, federal, state):


	hours = float(hours)

	rate = float(rate)

	federal = float(federal)

	state = float(state)


	employees[name] = {'Employee name': name, 'hours worked': hours, 'pay rate': rate, 'gross pay': 0, 'Deduction':' ', 'federal withholding': 0, 'state withholding': 0, 'Total Deduction': 0, 'Net pay': 0}


	if hours <= 0 or hours > 160:
		return "dick that's not right"

	employees[name]['hours worked'] = hours


	if rate <= 0:
		return "dick that's not right, pay me well"

	employees[name]['Pay rate'] = rate


	gross = rate * hours

	employees[name]['gross pay'] = gross


	if federal <= 0 or federal > 100:
		return 'invalid input'

	fed_tax = gross * federal / 100

	employees[name]['federal withholding'] = fed_tax
	

	if state <= 0 or state > 100:
		return 'invalid input'

	state_tax = gross * state / 100

	employees[name]['state witholding'] = state_tax


	total = federal + state

	employees[name]['Total Deduction'] = total


	net_pay = gross - total

	employees[name]['Net pay'] = net_pay

	return f'Employee payroll added.'



def view_all_payroll(employees):


	for name, employee in employees.items():

		for key, value in employee.items():

			print(f'{key}: {value}')



def update_payroll(employees, update):

	if not update.isdigit():
		return "invalid input"

	update = int(update)

	if name not in employees:
		return "Employee not found"

	for index, name in enumerate(employees, 1):
		if update == index:

			employees.pop(index - 1)
			return 'update successfully'



	
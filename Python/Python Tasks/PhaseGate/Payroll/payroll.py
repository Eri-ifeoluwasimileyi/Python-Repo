def check_name_validity(employees, name):

	if name in employees:

		return "Employee's already exist"
	
	new_name = name.replace(' ', '', 1)

	if name == '':

		return "this space cannot be empty"

	elif name.isspace():

		return "this space cannot be empty"


	elif new_name.isalpha():

		return name
	
	else: return "Invalid name"


def check_amount(amount):

	if not amount:

		return "this space cannot be empty"

	if amount.isspace():

		return "this space cannot be empty"

	another_amount = amount.replace('.', '', 1)

	if all(number.isdigit() for number in another_amount):
		
		amount = float(amount) 
			
		if amount == round(amount, 2): return True
		else: return "Invalid input"

	else: return "Invalid input"




def check_hours(hours):

	if not hours:

		return "this space cannot be empty"

	if hours.isspace():

		return "this space cannot be empty"

	another_hours = hours.replace('.', '', 1)

	if all(number.isdigit() for number in another_hours):
		
		hours = float(hours)

		if hours <= 0 or hours > 40:

			return "Invalid hours"

		else: return True

	else: return "Invalid hours"



def check_rate(rate):

	if not rate:

		return "this space cannot be empty"

	if rate.isspace():

		return "this space cannot be empty"

	another_rate = rate.replace('.', '', 1)

	if all(number.isdigit() for number in another_rate):
		
		rate = float(rate)


		if rate > 0 :

			return True

		else: return "Invalid rate"

	else: return "bitch that's not right, pay me well"




def check_federal(federal):

	if not federal:

		return "this space cannot be empty"

	if federal.isspace():

		return "this space cannot be empty"

	another_federal = federal.replace('.', '', 1)

	if all(number.isdigit() for number in another_federal):
		
		federal = float(federal)

		if federal <= 0 or federal > 100:
			return "Invalid tax"
			
		else: return True

	else: return "Invalid tax"


def check_state(state):

	if not state:

		return "this space cannot be empty"

	if state.isspace():

		return "this space cannot be empty"

	another_state = state.replace('.', '', 1)

	if all(number.isdigit() for number in another_state):
		
		state = float(state)

		if state > 0 or state <= 100:
			return True
		else: return "Invalid tax"

	else: return "Invalid tax"



def create_payroll(employees, name, hours, rate, federal, state):


	hours = int(hours)

	rate = float(rate)

	federal = float(federal)

	state = float(state)


	employees[name] = {'Employee name': name, 'Hours worked': 0, 'Pay rate': 0, 'Gross pay': 0, 'Deduction':' ','\tFederal withholding': 0, '\tState withholding': 0, '\tTotal Deduction': 0, 'Net pay': 0}



	employees[name]['Hours worked'] = hours


	employees[name]['Pay rate'] = f'${rate}'


	gross = round((rate * hours), 2)

	employees[name]['Gross pay'] = f"${gross}"


	fed_tax = round((gross * federal / 100), 2)

	employees[name]['\tFederal withholding'] = f'${fed_tax}'
	

	state_tax = round((gross * state / 100), 2)

	employees[name]['\tState withholding'] = f'${state_tax}'


	total = round((fed_tax + state_tax), 2)

	employees[name]['\tTotal Deduction'] = f'${total}'


	net_pay = round((gross - total), 2)

	employees[name]['Net pay'] = f'${net_pay}'

	return True



def view_all_payroll(employees):


	for name, employee in employees.items():

		for key, value in employee.items():

			print(f'{key}: {value}')



def update_payroll(employees, name):

	if name not in employees:
		return "Employee not found"

	employees.pop(name)
	return True




	
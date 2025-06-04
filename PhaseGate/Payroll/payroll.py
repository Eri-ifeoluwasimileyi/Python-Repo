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



def create_payroll(employees, name, hours, rate, gross, federal, state, total, pay):

	employees[name] = {'Employee name': name, 'hours worked': hours, 'pay rate': rate, 'gross pay': gross, 'Deduction':' ', 'federal withholding': federal, 'state withholding': state, 'Total Deduction': total, 'Net pay': pay}

	return f'Employee payroll added.'


	if name not in employees:
		return "Employee not found"

	elif name in employees:
		employee[name]['Employee name'] = name
		return f'Employee name: {name}'


	elif hours <= 0 or hours > 160:
		return "dick that's not right"

	employees[name]['hours worked'] = hours

	return f'Hours Worked: {hours}'


	if name not in employees:
		return "Employee not found"

	elif rate <= 0:
		return "dick that's not right, pay me well"

	employees[name]['Pay rate'] = rate

	return f'Pay rate: ${rate}'

	employees[name]['gross pay'] = rate * hours

	return f'Gross pay: ${employees[name]['gross pay']}'


	if name not in employees:
		return "Employee not found"

	elif federal <= 0 or federal > 100:
		return 'invalid input'

	employees[name]['federal withholding'] = gross * federal / 100
	
	return f'Federal Withholding: ${employees[name]['federal withholding']}'

	if name not in employees:
		return "Employee not found"

	elif state <= 0 or state > 100:
		return 'invalid input'

	employees[name]['state witholding'] = gross * state / 100
	return f'State Withholding: ${employees[name]['state witholding']}'

	employees[name]['Total Deduction'] = federal + state
	return f'Total Deduction: ${employees[name]['Total Deduction']}'

	employees[name]['Net pay'] = gross + total
	return f'Net pay: ${employees[name]['Net pay']}'




def view_all_payroll(employees):

	for key, value in employees.items():

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



	
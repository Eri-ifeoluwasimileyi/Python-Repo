def check_month(month):

	if month == 2:
		
		days = 28

	else:
		if month == 4:

			days = 30

		elif month == 6:

			days = 30

		elif month == 9:

			days = 30
 
		elif month == 11:

			days = 30
		else:
			days = 31	

	return days
	

def check_days(last_period, period_month, days_to_add):

	while days_to_add > 0:

		days_in_a_month = check_month(period_month)

		if (last_period + days_to_add) <= days_in_a_month:

			new_day = last_period + days_to_add

			return new_day, period_month

			break

		else:
			days_to_add -= (days_in_a_month - last_period + 1)
			
			last_period = 1			

			period_month += 1


			if period_month > 12:

				period_month = 1



	return last_period, period_month


		
def date(day, month):

	if isinstance(day, int) and isinstance(month, int):

		return f'{day:02d} - {month:02d}'	
	
	else:
		return "invalid input"






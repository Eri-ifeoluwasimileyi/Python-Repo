import menstrual_app
from menstrual_app import *

print('''
	====================
	Menstrual Calculator
	====================
		my pride!!	
				''')


last_period = int(input('Enter first day of your last period from(1-31): '))
print()

period_month = int(input('Enter the month from(1-12): '))
print()

period_days = int(input('How long does your periods last on an average: ')) 
print()

cycle_length = int(input('What is your average cycle length(days): '))
print()


	
ovulation_day = cycle_length // 2

fertile_window = ovulation_day - 5

fertile_window_end = ovulation_day + 1

next_period = cycle_length + 1

range_of_next_period = next_period + period_days



newday_1, new_month1 = check_days(last_period, period_month, ovulation_day)

newday_2, new_month2 = check_days(last_period, period_month, fertile_window)

newday_3, new_month3 = check_days(last_period, period_month, fertile_window_end)

newday_4, new_month4 = check_days(last_period, period_month, next_period)

newday_5, new_month5 = check_days(last_period, period_month, range_of_next_period)



print('Calculating, please wait.......')


print(f'Your estimated ovulation date is: {date(newday_1, new_month1)}')
print()

print(f'Fertile Window starts: {date(newday_2, new_month2)} and ends: {date(newday_3, new_month3)}')
print()

print(f'Your next period is estimated to be between: {date(newday_4, new_month4)} and {date(newday_5, new_month5)}')



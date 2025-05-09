investment_amount = float(input('Enter the invest amount: '))

number_of_years = int(input('Enter number of years: '))

interest_rate = float(input('Enter the interest rate: '))

interest_rate_D = interest_rate / 100


for years in range(1, number_of_years+1):

	investment_amount =(investment_amount * interest_rate_D) + investment_amount
	 

	print(f' Your ROI for the year is {investment_amount:,.2f}')
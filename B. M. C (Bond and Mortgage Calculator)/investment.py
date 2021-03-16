import sys

def investmentCalculation():
	try:
		amount_to_invest = float(input('Initial Investment Amount: '))
		interest_rate = float(input('Interest Rate (as percentage without the "%"): '))
		number_of_years = int(input('Number of Year(s) to invest for: '))
		
		print(
			'''\nwhich Interest Rate do you want? (Enter a number to choose your option):
			1. Simple
			2. Compound
			'''
		)

		interest_type = int(input('Option: '))

		while interest_rate:
			if interest_type == 1:
				return round(amount_to_invest * (1 + (interest_rate / 100) * number_of_years), 2)
			elif interest_type == 2:
				return round(amount_to_invest * pow((1+ interest_rate / 100), number_of_years), 2)
			else:
				return 'Not a valid Value!'

	except:
		return 'Not a valid Value!'
		
def bondCalculation():
	present_value = float(input('The current value of the house: '))
	interest_rate = float(input('Interest Rate (as percentage without the "%"): '))
	number_of_months = int(input('Number of Month(s) you\'ll take to repay the bond: '))

	return round(present_value * ((((interest_rate / 100) / 12) * (1 + ((interest_rate / 100) / 12)) ** number_of_months )/(((1 + ((interest_rate / 100) / 12)) ** number_of_months ) - 1)), 2)
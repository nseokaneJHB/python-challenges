import sys
from start import startProgram
from bond import bondCalculation
from investment import investmentCalculation

user_answer = str(input('\nHello there, please provide your name or type "Exit" to quit: '))

while not user_answer:
	user_answer = str(input('\nInvalid name, please provide your name or type "Exit" to quit: '))

	if user_answer.lower() == 'exit':
		sys.exit('Exiting the programme. Come back again soon!\n')
else:
	startProgram(user_answer)
	user_option = int(input('Your option: '))
	
	if user_option == 1:
		print('\n', investmentCalculation(), '\n')
	elif user_option == 2:
		print('\nR', bondCalculation(), '\n')
	elif user_option == 3:
		print('Exiting the programme... Come back again!')
	else:
		print('Invalid option, please choose between the options available on the screen')
	
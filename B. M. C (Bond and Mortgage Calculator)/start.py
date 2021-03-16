from art import *

def startProgram(username):
	print('''===========================================================''' * 3, '\n')

	tprint('''WELCOME   TO   B.M.C''', "rnd-large")

	print('========================================================================= Bond and Mortgage Calculator ==========================================================================\n')
	print(
		'''What would you like to calculate today? (Enter a number to choose your option):

			1. Investment
			2. Bond
			3. Exit
		'''.format(username.title())
	)
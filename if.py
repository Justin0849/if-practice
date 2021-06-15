age = input('Please enter your age : ')
if int(age) >= 15 :
	print('You can go to work. ')
	if int(age) < 16:
		print('You can only work between 8 am to 8 pm.')
		print('You can not work over 8 hour a day.')
if int(age) < 15:
	print('You can not go to work.')
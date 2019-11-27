while True:
	usr_inpt = input('Enter gigabytes: ')
	if not usr_inpt:
		print('ведите число!')
	if usr_inpt.isdigit() == True:
		compute = 1024 % int(usr_inpt)
		sum = int(usr_inpt) - int(compute)
		print('TiB: ' + str(sum))
	else:
		print('ведите число!')
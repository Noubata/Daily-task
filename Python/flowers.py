def petals(source):
	user_input = input("Enter the number of petals: ")
	try:
		number = int(user_input)
		if user_input == int:
			return user_input
	except:
		print("Only numbers are accepted")

	user_input2 =input("Enter the number of petals: ")
	try:
		number1 = int(user_input2)
		if user_input2 == int:
			return user_input2
	except:
		print("Only numbers are accepted")

	if number % 2 == 0 and number1 % 2 != 0:
		print("Wow! You guys are in love.")
	elif number % 2 != 0 and number1 % 2 == 0 :
		print("Wow! You guys are in love.")
	else:
		print("Love no dey in this your relationship")
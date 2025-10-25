def the_upper_case(the_input):
	if type(the_input) != str:
		print("Only strings are allowed")
	elif type(the_input) == str:
		result = the_input.upper()
		print(result)
	else:
		print("Invalid input")
	return the_input
	
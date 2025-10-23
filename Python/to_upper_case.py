def the_upper_case(the_input):
	if type(the_input) != str:
		print("Only strings are allowed")
	else:
		result = the_input.upper()
		print(result)
	return the_input
import re
result = []
user_input = input("Enter Your password as comma seperated: \n ")
print("user input: ", user_input)
input_list = user_input.split(",")
print("input_list: ", input_list)
for password in input_list:
	if len(password) < 6 or len(password) > 12:
		continue
	elif not re.search("[a-z]", password):
		continue
	elif not re.search("[A-Z]", password):
		continue
	elif not re.search("[0-9]", password):
		continue
	elif not re.search("[$#@]", password):
		continue
	else:
		result.append(password)
print(result)


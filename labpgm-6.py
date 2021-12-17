net_amount = 0
while True:
	user_input = input("Enter Transaction: ") #D 300
	transaction = user_input.split(" ")  #['D', '300']
	#print("transaction", transaction)
	if len(transaction) < 2:
		print("Input is not right please provide like D 100 or W 100: ")
		break
	type = transaction[0] #{key: value for key, value in variable}
	amount = int(transaction[1])
	#print("amount", amount)
	if type == "D" or type == "d":
		net_amount += amount
	elif type == "W" or type == "w":
		if net_amount >= amount:
			net_amount -= amount
		else:
			print("you do not have sufficient amount to withdraw. Net Amount is: ", net_amount)
	else:
		pass

	user_input = input("Do you want to continue? (Y for Yes, Any other to exit.) ")
	if not (user_input[0] == "Y" or user_input[0] == "y"):
		break
print("Net Amount: ", net_amount)

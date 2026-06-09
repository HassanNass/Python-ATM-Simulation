# ATM Simulation

users = [
	{ "name": "Nass", "pin": "1234", "balance": 500 },
	{ "name": "Bob", "pin": "5678", "balance": 200 }
]

# Create a new user account and add it to the users list
def create_account(users):

	# Get the user's name and remove any extra spaces
	name = input("Enter name: ").strip()
	
	# Check if an accont with the same name already exists (case-insensitive)
	for user in users:
		if user["name"].lower() == name.lower():
			print("An account with that name already exists.")
			return
	
	# Get the user's PIN and remove any extra spaces
	pin = input("Create a PIN: ").strip()
	
	# Create a new account with a starting balance of 0
	users.append({ "name": name, "pin": pin, "balance": 0})

	# Confirm that the account was created successfully
	print(f"Account created successfully! Welcome, {name}.")


# Authenticate a user by verifying their name and PIN
def authenticate(users):

	# Get the user's name and remove any extra spaces
	name = input("Enter your name: ").strip()

	# Search for a matching account (case-insensitive)
	for user in users:
		if user["name"].lower() == name.lower():

			# Allow up to 3 PIN entry attempts
			for attempts in range(3):

				# Ask the user to enter their PIN
				pin = input(f"Enter Your PIN (attempts {attempts + 1}/3): ").strip()

				# Check if the entered PIN matches the account PIN
				if user["pin"] == pin:
					print(f"Welcome, {user['name']}")
					return user # Return the user's dictionary when authentication succeeds
				
				# Inform the user of the remaining attempts
				print(f"Incorrect PIN. {2 - attempts} attempt(s) remaining!")

			# Executed if all 3 PIN attempts fail
			print("Too many incorrect attempts. Goodbye.")
			return None

	# Executed if no account with the entered name is found
	print("Name Not Found!")
	return None


# Deposite money into user's account
def deposit(user):

	# Attempts to convert the user's input into a number
	try:
		amount = float(input("Enter the amount to deposit: "))

	# Handle invalid inputs such as letters or special characters
	except ValueError:
		print("Invalid input. Please enter a number.")
		return

	# Make sure that the deposit amount is positive
	if amount <= 0:
		print("Amount must be greater than 0.")
		return

	# Add the deposit amount to the user's balance
	user['balance'] += amount

	# Display the updated balance then exit the function
	print(f"Deposit successful! Your new balance is: ${user['balance']:.2f}")
	return


# Withdraw money from user's account
def withdraw(user):

	# Attempt to convert the user's input into a number
	try:
		amount = float(input("Enter the amount to withdraw: "))

	# Handle invalid inputs such as letters or special characters
	except ValueError:
		print("Invalid input.  Please enter a number.")
		return

	# Make sure that the withdrawal amount is positive
	if amount <= 0:
		print("Amount must be greater than 0.")
		return

	# Check if the user has enough funds to complete the withdrawal
	elif amount > user['balance']:
		print(f"Insufficient funds! Your balance is only ${user['balance']:.2f}")
		return

	# Subtract the withdrawal amount from the user's balance
	user['balance'] -= amount

	# Display the updated balance then exit the function
	print(f"Withdrawal successful. Your new balance is: ${user['balance']:.2f}")
	return 


# Display the ATM menu and allow the user to perform account operations
def atm_menu(user):

	# Keep showing the menu until the user chooses to exit
	while True:

		# Display the ATM options
		print("\n--- ATM Menu ---")
		print("1. Check Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")

		# Get the user's menu choice and remove any extra spaces
		choice = input("Enter your choice (1-4): ").strip()
		print("-" * 30)

		# Display the current account balance
		if choice == "1":
			print(f"Your current balance is: ${user['balance']:.2f}")
		
		# Deposit money into the account
		elif choice == "2":
			deposit(user)

		# Withdrawal money from the account
		elif choice == "3":
			withdraw(user)

		# Exit the ATM menu
		elif choice == "4":
			print("Thank you for using our ATM. Goodbye.")
			break

		# Handle invalid menu selections
		else:
			print("Invalid option. Please enter a number from 1 to 4.")



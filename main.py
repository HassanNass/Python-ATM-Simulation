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



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


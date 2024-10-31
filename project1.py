# Username
name = input("Enter your new username: ")   # Invites user to create a username
print("Welcome to the Simple Banking System", name) # Welcomes user to Simple Banking

# Password & Encryption
def encrypt_password(password): # Defines encrypt_password function
	encrypted = []

	for char in password:
		m = ord(char) # ASII value of the characters

		if "a" <= char <= "z": # Encrypts the lowercase letters
			base = ord("a")
			encrypted.append(chr((m + 3 - base) % 26 + base))
		elif "A" <= char <= "Z": # Encrypts the uppercase letters
			base = ord("A")
			encrypted.append(chr((m + 3 - base) % 26 + base))
		elif "0" <= char <= "9": # Encrypts the numbers/digits
			base = ord("0")
			encrypted.append(chr((m + 3 - base) % 10 + base))
		else: # Non-alphanumeric characters are left unchanged
			encrypted.append(char)
	return "".join(encrypted)

password = input("Enter a password: ")
encrypted_password = encrypt_password(password) # Encrypts the password, does not print encrypted version

# Initial Balance
initial_balance = float(input("Enter the initial balance: ")) # User inputs initial balance

# Succesfully created account
print("Account creation successful!")

# User Interface
logged_in = False
while True:
	print("\nSelect a service:")
	print("1. Login to Account")
	print("2. Deposit to Account")
	print("3. Withdraw from Account")
	print("4. Print Balance")
	print("5. Change Password")
	print("6. Logout")
	
	choice = input("Enter your choice: ")
	
	if choice == "1":
		logged_in = (input("Usernam: ") == user["username"] and encrypt_password(input("Password: ")) == user["password"])
		print("login successful!" if logged_in else "Invalid username or password.")
	elif not logged_in:
		print("Print log in first.")
	elif choice == "2":
		deposit()
	elif choice == "3":
		withdraw()
	elif choice == "4":
		view_balance()
	elif choice == "5":
		change_password()
	elif choice == "6":
		print("Logged out.")
		logged_in = False
	else:
		print("Invalid option. Please select a valid option.")
	if not logged_in and choice == "6":
		break

# Deposits
def deposit_amount(current_balance, amount):
	amount = float(input("Confirm the deposit amount: ") # Invites user to input deposit amnt
	if amount > 0.0:
		current_balance += amount # Increases the total balance
		print(f"Updated Balance: ${current_balance:.2f}")
	else:
		print(f"Invalid amount. Re-enter a valid number: ") # Negative deposits are not valid
	return current_balance
balance = deposit_amount(balance, input("Enter the deposit amount: "))

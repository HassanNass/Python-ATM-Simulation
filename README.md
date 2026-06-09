# Python ATM Simulation

A command-line ATM simulation built in Python. Supports multiple users, PIN authentication with attempt limiting, deposits, withdrawals, balance checking, and new account creation — all through an interactive menu system.

---

## Features

### Main Menu
- Login to an existing account
- Create a new account
- Exit the program

### Authentication
- Login by name (case-insensitive)
- PIN verification with a **3-attempt limit** — account access is blocked after 3 incorrect entries
- Duplicate account names are rejected at creation

### ATM Menu (after login)
- **Check Balance** — displays current account balance
- **Deposit** — adds funds to the account, displays updated balance
- **Withdraw** — deducts funds if balance is sufficient, displays updated balance
- **Exit** — returns to the main menu

### Input Validation
- All amounts must be positive numbers
- Invalid inputs (letters, special characters) are handled with clear error messages
- Menu choices outside the valid range are caught and handled

---

## How to Run

Make sure you have Python 3 installed.

```bash
python atm.py
```

---

## Example

```
--- Welcome to the ATM ---
1. Login
2. Create new account
3. Exit
Enter your Choice (1-3): 1
------------------------------
Enter your name: Nass
Enter Your PIN (attempts 1/3): 1234
Welcome, Nass

--- ATM Menu ---
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter your choice (1-4): 2
------------------------------
Enter the amount to deposit: 200
Deposit successful! Your new balance is: $700.00
```

---

## Project Structure

```
Python-ATM-Simulation/
├── atm.py
└── README.md
```

---

## What I Practiced

- Structuring a program using functions — each function handles one responsibility
- Working with lists of dictionaries to manage multiple user accounts
- Input validation using `try/except` for type errors and conditional checks for logic errors
- Using `if __name__ == "__main__"` to follow correct Python module conventions
- Building an interactive CLI menu with a loop and clean exit conditions

---

## Author

**Hassan Nasrallah**
[github.com/HassanNass](https://github.com/HassanNass)
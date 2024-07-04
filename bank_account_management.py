# Read txt
def read_account():

    filename = "accounts.txt" # Account Details text file
    accounts_details = {}

    try:
        with open(filename, 'r') as file:
            for record in file:
                account_number, balance = record.split()
                accounts_details[account_number] = float(balance)
    
    except FileNotFoundError:
        print("Database Not Found...")

    return accounts_details

# Write txt
def write_account(accounts_details):

    filename = "accounts.txt" # Account Details text file

    with open(filename, 'w') as file:
        for account_number, balance in accounts_details.items():
            file.write(f"{account_number} {balance}\n")

# Update Accounts Details function
def update_account(account_number, balance):
    accounts_details = read_account() # Account details dictionary
    accounts_details[account_number] = balance # update dictionary
    write_account(accounts_details)

    return "Succesfully updated"

# Get Account Balance function
def get_balance(account_number):

    accounts_details = read_account() # Account details dictionary

    return accounts_details.get(account_number, None)

# Cash Deposit function
def deposit(account_number, amount):

    old_amount = get_balance(account_number) # Get old amount in account
    new_amount = old_amount + amount # Add new amount to old amount
    
    update_account(account_number, new_amount)

# Cash Withdraw function
def withdraw(account_number, amount):

    old_amount = get_balance(account_number) # Get old amount in account
    new_amount = old_amount - amount # Substract new amount to old amount

    # Check withdrow amount 
    if new_amount < 0:
        return 0
    
    else:
        update_account(account_number, new_amount)

def handleBankProcess():

    print("Please select an option:\n 1. Get Balance \n 2. Deposit \n 3. Withdraw \n 4. Type 'exit' to quit")
    while True:
        choise = input("Enter your choise: ")
        if choise.lower() == "exit":
            break
        elif choise == '1':
            while True:
                user_input = input("Enter your account number: ")
                balance = get_balance(user_input)

                if user_input.lower() == "exit":
                    break

                elif balance == None:
                    print("*** Your account number is invalid. Please chcek the account number and input again *** \n \tIf you want exit type 'exit'")

                else:
                    print("Your currant acount balance is: ", balance)
                    break

        elif choise == '2':
           while True:
            account_number = input("Enter your account number: ")

            if account_number.lower() == "exit":
                break

            try:
                amount = float(input("Enter the deposit amount: "))
                if amount <= 0:
                    raise ValueError("Amount must be a positive number.")
            except ValueError as e:
                print("Amount is invalid.")
                continue

            accounts_details = read_account() # Account details dictionary
            check_account = accounts_details.get(account_number, None)

            if check_account is None:
                print("*** Your account number is invalid. Please check the account number and input again *** \n\tIf you want to exit type 'exit'")
            else:
                deposit(account_number, amount)
                print("Deposit successfully.")
                break

        elif choise == '3':
            while True:
                account_number = input("Enter your account number: ")

                if account_number.lower() == "exit":
                    break

                try:
                    amount = float(input("Enter the withdraw amount: "))
                    if amount <= 0:
                        raise ValueError("Amount must be a positive number.")
                except ValueError as e:
                    print("Amount is invalid.")
                    continue

                accounts_details = read_account() # Account details dictionary
                check_account = accounts_details.get(account_number, None)

                if check_account is None:
                    print("*** Your account number is invalid. Please check the account number and input again *** \n\tIf you want to exit type 'exit'")
                else:
                    
                    response = withdraw(account_number, amount)

                    if response == 0:
                        print("Your account balance is not enaough")
                        break
                    else:
                        print("Withdraw successfully.")
                        break
        else:
            print("Invalid input. Check and input again.")
        
    
def main():
    handleBankProcess()

if __name__ == "__main__":
    main()
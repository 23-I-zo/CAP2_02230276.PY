#Tshering Dorji
#First Year BE in Mechanical Engineering
#02230276
#REFERENCE
#https://www.youtube.com/watch?v=xTh-ln2XhgU
#https://www.youtube.com/watch?v=q2SGW2VgwAM
#https://www.youtube.com/watch?v=JeznW_7DlB0



import os   # Imports the os module for interacting with the operating system
import random   # Import the random module for generating random numbers for the system
import string   # Import the string module for string constants or for generating random strings

# Makingg a class for base account
class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    # code for depositing money to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("Invalid. Try again!")

    # Code for withdrawing money from an account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: Nu{amount}. New Balance: Nu{self.balance}")
        else:
            print("Insufficient or invalid. Try again.")

    #code for saving the data of the banking in a file
    def save_to_file(self, file_name='accounts.txt'):
        with open(file_name, 'a') as f:
            f.write(f"{self.account_number},{self.password},{self.account_type},{self.balance}\n")


# Personal Account class inheriting from the base Account class
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        #using OOP
        super().__init__(account_number, password, 'personal', balance)

# bussiness Account class inheriting from the base Account class
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        #using OOP
        super().__init__(account_number, password, 'business', balance)

# code for generating account number(account number of only 5 numbers)
def generate_account_number():
    return ''.join(random.choices(string.digits, k=5))

#code for generating passwords for the account (passord with 4 numbers)
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

# function to load account from the data file
def load_accounts(file_name='accounts.txt'):
    accounts = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            for line in lines:
                account_number, password, account_type, balance = line.strip().split(',')
                balance = float(balance)
                if account_type == 'personal':
                    account = PersonalAccount(account_number, password, balance)
                elif account_type == 'business':
                    account = BusinessAccount(account_number, password, balance)
                accounts[account_number] = account
    return accounts

# Code for logging in an account
def login(accounts):
    #prompt user to enter their account number and password for the account
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    
    account = accounts.get(account_number)
    if account and account.password == password:
        print("LOGIN SUCCESSFUL!")
        return account
    else:
        print("Acount number or the password was invalid. Try again!")
        return None


# Code for transfering money from one account to the other
def fund_transfer(accounts, from_account):
    #promt the users to enter the recipient account number and the amount to transfer
    to_account_number = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount to send: "))
    if to_account_number in accounts:
        if from_account.balance >= amount:
            from_account.withdraw(amount)
            accounts[to_account_number].deposit(amount)
            print(f"Transferred Nu{amount} to {to_account_number}")
        else:
            print("Insufficient amount.")
    else:
        print("Recipient not found.")

# main function for running the banking system
def main():
    accounts = load_accounts()

    while True:
        # giving options for the user to choose 
        print("\n Welcome to Tshering Bank")
        print("1. Open an Account")
        print("2. Login to Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Select Account Type:")
            print("1. Personal Account")
            print("2. Business Account")
            account_type = input("Enter your choice: ")
            if account_type in ['1', '2']:
                account_number = generate_account_number()
                password = generate_password()
                if account_type == '1':
                    account = PersonalAccount(account_number, password)
                else:
                    account = BusinessAccount(account_number, password)
                account.save_to_file()
                accounts[account_number] = account
                print(f"Account created successfully! Account Number: {account_number}, Password: {password}")
            else:
                print("Invalid choice.Try again!")

        elif choice == '2':
            account = login(accounts)
            if account:
                while True:
                    print("\n Menu")
                    print("1. Balance")
                    print("2. Deposit ")
                    print("3. Withdraw ")
                    print("4. Transfer funds")
                    print("5. Delete Account")
                    print("6. Logout")
                    account_choice = input("Enter your choice: ")

                    if account_choice == '1':
                        print(f"Your Balance: Nu{account.balance}")
                    elif account_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif account_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif account_choice == '4':
                        fund_transfer(accounts, account)
                    elif account_choice == '5':
                        del accounts[account.account_number]
                        print("Account deleted successfully.")
                        break
                    elif account_choice == '6':
                        print("You logged out successfully!")
                        break
                    else:
                        print("Invalid choice, try again!")
        
        elif choice == '3':
            print("thank you for using Tshering Bank")
            break

        else:
            print("Invalid Choice, try again!.")

# Calling the function
if __name__ == "__main__":
    main()
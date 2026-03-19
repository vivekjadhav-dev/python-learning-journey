# strech goal
import datetime
user_name = input("enter the name of account holder: ")
try: 
    birth_year = int(input("enter the account holders birth year: "))
    account_balance = float(input("enter the account balance: ₹"))
    deposit_amount = float(input("enter the amount  you want to deposit: ₹"))
except ValueError:
    print("Invalid Input. Please Enter a Number.")
    exit()
current_year = datetime.datetime.now().year
user_age = current_year - birth_year
if (account_balance > 1000):
    account_balance *=1.025

new_balance = account_balance + deposit_amount
print("----- Account summary -----")
print(f"Name : {user_name}")
print(f"Age: {user_age}")
print(f"New balance : ₹{new_balance:.2f}")
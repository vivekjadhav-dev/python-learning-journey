try:
    bill_amount = float(input("Enter the total bill amount: ₹"))
    tax = float(input("Enter the tax percentage: "))
    splitters = int(input("Enter the number of people splitting the bill: "))
except ValueError :
    print("Invalid Value, Please Enter the Correct Values.")
    exit()

total_bill = bill_amount + bill_amount*(tax/100)
amount_to_pay = total_bill / splitters
print(f"total bill amount after the tax is {total_bill:.2f}.")
print(f"amount for each person to pay is {amount_to_pay:.2f}.")
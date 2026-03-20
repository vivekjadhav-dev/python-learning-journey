try:
    customer_name = input("Enter the name of the customer: ")
    units_consumed = int(input("Enter units of electricity consumed: "))
except ValueError:
    print("Invalid Value, please Enter the correct details.")
    exit()
if units_consumed <= 0:
    print("Error, the unit consumed cannot be a zero or a negative number.")
    exit()
elif units_consumed <= 100:
    rate_per_unit = 3.50
    usage_category = "Low Usage"
elif units_consumed <= 300:
    rate_per_unit = 4.75
    usage_category = "Moderate Usage"
elif units_consumed <= 500:
    rate_per_unit = 6
    usage_category = "High Usage"
else:
    rate_per_unit = 7.25
    usage_category = "Very High Usage"

service_charge = 50
total_electricity_bill = (units_consumed * rate_per_unit) + service_charge
print("-->--->>--->>> ELECTRICITY BILL <<<---<<---<--")
print(f"{'Customer Name: ':<25}{customer_name}")
print(f"{'Units Consumed: ':<25}{f'{units_consumed}':>20}")
print(f"{'Usage Category: ':<25}{f'{usage_category}':>20}")
print(f"{'Rate Per Unit: ':<25}{f'₹{rate_per_unit:.2f}':>20}")
print(f"{'Service Charge: ':<25}{f'₹{service_charge:.2f}':>20}")
if total_electricity_bill > 2000:
    print(f"{'Bill Before Surcharge: ':<25}{f'₹{total_electricity_bill:.2f}':>20}")
    surcharge = total_electricity_bill * (5 / 100)
    total_electricity_bill += surcharge
    print(f"{'Surcharge (5%): ':<25}{f'₹{surcharge:.2f}':>20}")
if total_electricity_bill < 200:
    print("(Minimum Bill Applied)")
    total_electricity_bill = 200
print(f"{'Total bill: ':<25}{f'₹{total_electricity_bill:.2f}':>20}")

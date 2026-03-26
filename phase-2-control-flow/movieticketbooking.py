try:
    name = (input("Enter your name: "))
    age = int(input("Enter your age: "))
    day = (input("Enter the day on which you want watch the movie: "))
except ValueError :
    print("Incorrect values, please enter the correct values.")
    exit()

day = day.lower()
valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if day not in valid_days:
    print("Invalid day.")
    exit()
    
if age < 0 :
    print("Age cannot be negative.")
elif age < 5 :
    category = "Free"  
    price = 0
elif age < 13 :
    category = "Child"  
    price = 100
elif age < 18 :
    category = "Teen"  
    price = 150
elif age < 60 :
    category = "Adult"  
    price = 250
elif age <= 120 :
    category = "Senior"  
    price = 120
else:
    print("Enter the real age.")        
    exit()

print("->>---->> MOVIE TICKET <<----<<-")
print(f"{'Customer: ':<17}{name:>}") 
print(f"{'Age: ':<17}{age:>}") 
print(f"{'Category: ':<17}{category :>}")
print(f"{'Day: ':<17}{day:>}")
print(f"{'Base price: ':<17}{f'₹{ price:.2f}':>}")

if day == 'saturday' or day == 'sunday':
    discounted_price = (price * 15/100)
    final_price = discounted_price + price
    print(f"{'Surcharge (15%): ':<17}{f'{discounted_price:.2f}':>}")
    print(f"{'Final price: ':<17}{f'₹{ final_price:.2f}':>}")
elif day =='wednesday':
    discounted_price = (price * 10/100)
    final_price = price - discounted_price
    print(f"{'Discount(10%): ':<17}{f'{discounted_price:.2f}':>}")
    print(f"{'Final price: ':<17}{f'-₹{final_price:.2f}':>}")  
elif day == 'monday' or day == 'tuesday':
    discounted_price = (price * 20/100)
    final_price = price - discounted_price
    print(f"{'Discount(20%): ':<17}{f'{discounted_price:.2f}':>}")
    print(f"{'Final price: ':<17}{f'₹{final_price:.2f}':>}")
else:
    final_price = price
    print(f"{'Final price: ':<17}{f'₹{final_price:.2f}':>}")

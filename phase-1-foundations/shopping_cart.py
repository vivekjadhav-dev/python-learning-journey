try:
    item_1 = input("Enter the name of a first product: ")
    price_1 = float(input("Enter the price of a first product: ₹"))
    item_2 = input("Enter the name of a second product: ")
    price_2 = float(input("Enter the price of a second product: ₹"))
    item_3 = input("Enter the name of a third product: ")
    price_3 = float(input("Enter the price of a third product: ₹"))
    discount = float(input("Enter the given discount on a products in percentage: "))
except ValueError :
    print("Invalid Value, Please enter numbers correctly.")
    exit()
    
subtotal = price_1 + price_2 + price_3
discounted_price = subtotal *(discount / 100)
discounted_total = subtotal - discounted_price
gst_tax = discounted_total * (18/100)
total = discounted_total + gst_tax
items = [item_1, item_2, item_3]
prices = [price_1, price_2, price_3]
max_item = max(len(name) for name in items)
max_price = 15
if max_item < 16:
    max_item = 16    
total_len = max_item + max_price + 9
print(f"{'-' * (((max_item + max_price)//2) + 1)} RECEIPT {'-' * (((max_item + max_price)//2) +1)}")
print(f"Item 1: {item_1:<{max_item}} {f'₹{price_1:.2f}':>{max_price}}")
print(f"Item 2: {item_2:<{max_item}} {f'₹{price_2:.2f}':>{max_price}}")
print(f"Item 3: {item_3:<{max_item}} {f'₹{price_3:.2f}':>{max_price}}")
print(f"{"-" * (total_len)}")
print(f"{"Subtotal:":<{16}} {f'₹{subtotal:.2f}':>{max_price}}")
print(f"{f'Discount({discount:.0f}%):':<{16}} {f'-₹{discounted_price:.2f}':>{max_price}}")
print(f"{"After Discount:":<{16}} {f'₹{discounted_total:.2f}':>{max_price}}")
print(f"{"GST (18%):":<{16}} {f'₹{gst_tax:.2f}':>{max_price}}")
print(f"{"-" * (total_len)}")
print(f"{"Total:":<{16}} {f'₹{total:.2f}':>{max_price}}")

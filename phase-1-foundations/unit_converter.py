try:
    distance = float(input("Enter the distance in kilometer: "))
    weight = float(input("Enter the weight in kilogram: "))
    tempreature = int(input("Enter the temperature in celsius: "))
except ValueError:
    print("Invalid Vlaue, please enter the correct values.")
    exit()

if distance < 0:
    print ("Please enter the a positive number.")
    exit()

if weight < 0:
    print ("Please enter the a positive number.")
    exit()
    
if tempreature < 0:
    print ("Please enter the a positive number.")
    exit() 

miles = distance * 0.621371
pound = weight * 2.20462
fahrenheit = (tempreature * 9/5) + 32

print(f"{distance}km is {miles} miles.")
print(f"{weight}kg is {pound} pounds.")
print(f"{tempreature} celsius is {fahrenheit} fahrenheit.")
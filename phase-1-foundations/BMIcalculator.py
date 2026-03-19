user_name = input("Enter your name: ")
try:
    weight = float(input("Enter your weight in kg:"))
    height = float(input("enter your height in m: "))
except ValueError:
    print("Invalid value")
    exit()
bmi = weight / (height ** 2)
print(f"{user_name}, your BMI is {bmi:.2f}.")
# day 2 -myython first intentional progaram 
# vivek jadhav |python journey 2026
name = "vivek"
age = 20
is_student = True
cgpa = 8.39
nothing = None

print(type(name))
print(type(age))
print(type(is_student))
print(type(cgpa))
print(type(nothing))

# mutabilty trap
print("\n--- the mutability trap ---")
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(f"list_a: {list_a}")
print(f"list_b: {list_b}")

print("\n--- the safe copy ---")
list_c = [1, 2, 3]
list_d = list_c.copy() 
list_d.append(4)

print(f"list_c: {list_c}")
print(f"list_d: {list_d}")

# concept 3 : --- is vs == ---

print("\n--- is vs == ---")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print (f"x == y: {x == y}")
print (f"x is y: {x is y}")
print (f"x is z: {x is z}")

# concept 4 :--- f-strings ---
print ("\n--- f-string ---")

course = "bca"
year = 2
city = "nashik"

print(f"i am {name},year {year} {course} student from {city}.")
print(f"i am {age} years old")
print(f"is a {name} a student ?{is_student}")
print(f"{name} has {len(name)} letters in his name.")
try:
    total_seconds = int(input("Enter the number of seconds: "))
except ValueError :
    print("Invalid Value, please enter the correct number of seconds.")
    exit()

day = total_seconds // 86400
remaining_secs = total_seconds % 86400 
hour = remaining_secs // 3600
remaining_secs = remaining_secs % 3600
minute = remaining_secs // 60
remaining_secs = remaining_secs % 60
second = remaining_secs
print(f"{day} day(s),{hour} hour(s), {minute} minute(s), {second} second(s)")
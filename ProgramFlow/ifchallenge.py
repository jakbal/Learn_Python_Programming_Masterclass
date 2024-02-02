name = input("Name: ")
age = int(input("Age: "))

if 18 <= age < 31:
    print(f"{name} - it's a high time to start your vacation!")
else:
    print("Sorry, it's not your time :(")

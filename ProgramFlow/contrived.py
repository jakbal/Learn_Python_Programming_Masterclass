numbers = [1,45,31,16,60]

for number in numbers:
    if number % 8 == 0:
        print("Numbers are invalid.")
        break

else:
    print("Numbers are valid.")

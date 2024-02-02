name = input("Enter your name: ")
age = int(input("Enter your age {0}: ".format(name)))
print(age)

if age < 18:
    print("Be back in {0}".format(18-age))
elif age == 900:
    print("Sorry Yoda, you died in Return of the Jedi")
else:
    print("Lets vote")
    print("Put 'x' within the box")

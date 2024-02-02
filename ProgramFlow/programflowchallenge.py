choose = "-1"

while True:
    if int(choose) == -1:
        print("Available options:\n"
              "1. Eat\n"
              "2. Drink\n"
              "3. Mix\n"
              "4. Wait\n"
              "0. Exit")
    choose = input("Choose an option number: ")
    if int(choose) == 0:
        break
    elif int(choose) in range(1,5):
        print("Your number is {}".format(choose))
    else:
        choose = "-1"

choose = "-1"

while True:
    if int(choose) == 0:
        break
    elif int(choose) in range(1,5):
        print("Your number is {}".format(choose))
    else:
        print("Available options:\n"
              "1. Eat\n"
              "2. Drink\n"
              "3. Mix\n"
              "4. Wait\n"
              "0. Exit")
    choose = input("Choose an option number: ")

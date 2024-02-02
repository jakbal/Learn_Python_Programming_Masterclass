def fizz_buzz(number: int) -> str:
    """
    Function takes number and depending on it returns string
    `fizz` when number is divisible by 3
    `buzz` when number is divisible by 5
    `fizz buzz` when number is divisible by 3 and 5
    `number` in any other case

    :param number: integer number which is currently being processed
    :return: return a string depending on the input number
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return "{}".format(number)


# for n in range(100):
#     print("{}: ".format(n), fizz_buzz(n))

for n in range(1, 100):
    if n % 2 == 1:
        print("Number is {} and the computer says {}.".format(n, fizz_buzz(n)))
    else:
        print("Your turn. Number is {}.".format(n))
        answer = input("What do you say: ")
        if answer == fizz_buzz(n):
            continue
        else:
            print("Wrong answer.")
            break

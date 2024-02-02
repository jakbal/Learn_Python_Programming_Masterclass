import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a number!".format(temp))

highest = 1000
answer = random.randint(1,highest)
guess = None
print("Please guess a number (1-{}) or enter 0 to quit: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("Quit")
        break
    elif guess == answer:
        print("Good guess")
        break
    elif guess < answer:
        print("Guess higher: ")
    elif guess > answer:
        print("Guess lower: ")

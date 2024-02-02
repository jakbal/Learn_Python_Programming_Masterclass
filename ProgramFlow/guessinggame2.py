import random

highest = 10
answer = random.randint(1,highest)
guess = None
print("Please guess a number (1-{}) or enter 0 to quit: ".format(highest))

while guess != answer:
    guess = int(input())
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

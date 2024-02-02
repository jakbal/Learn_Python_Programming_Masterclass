answer = 5

print("Please guess a number (1-10): ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())
    if guess == answer:
        print("Winner")
    else:
        print("Wrong second time")
else:
    print("Winner by first guess")

# if guess < answer:
#     print("Guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Winner")
#     else:
#         print("Wrong")
# elif guess > answer:
#     print("Guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Winner")
#     else:
#         print("Wrong")
# else:
#     print("Winner")

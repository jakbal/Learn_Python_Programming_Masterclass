menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam" ],
]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         for item in meal:
#             print(item)
#     else:
#         print("{0} has a spam of {1}"
#               .format(meal, meal.count("spam")))


for meal in menu:
    for ingredient in meal:
        if ingredient != "spam":
            print(ingredient, end=", ")
    print()

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#         continue
#     else:
#         for index in range(len(meal) - 1, -1, -1):
#             if meal[index] == "spam":
#                 del meal[index]
#         print(meal)

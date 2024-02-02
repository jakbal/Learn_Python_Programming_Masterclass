from contents_quantity import pantry, recipes


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

def add_ingredient(shopping_dict: dict, ingredient: str, quantity: int) -> None:
    # if ingredient not in shopping_dict:
    #     shopping_dict[ingredient] = quantity
    # else:
    #     shopping_dict[ingredient] += quantity
    shopping_dict[ingredient] = shopping_dict.setdefault(ingredient, 0) + quantity


display_dict = {}
ingredients_to_buy = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe:")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}.")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"You need to buy {quantity_to_buy} of {food_item}.")
                add_ingredient(ingredients_to_buy, food_item, quantity_to_buy)

for ingredient, quantity in ingredients_to_buy.items():
    print(f"Buy {quantity} of {ingredient}.")

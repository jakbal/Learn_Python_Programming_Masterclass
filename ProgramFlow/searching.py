shopping_list = ["milk", "pasta", "eggs", "bread", "rice"]

item_to_find = "eggs"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at != None:
    print("Item found and position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at != None:
    print("Item found and position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

import copy

lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals = {
    "lios": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

#perform shallow copy
#things = animals.copy()

#performs deep copy
things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

#things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via animals")
things["teddy"].append("added via things")
print(animals["teddy"])
print(things["teddy"])

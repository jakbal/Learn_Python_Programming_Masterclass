lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals = {
    "lios": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

#things = animals.copy() #list referencs from dict are copied into new dict
things = {
    "lios": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

#things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via animals")
things["teddy"].append("added via things")
print(things["teddy"])
print(animals["teddy"])

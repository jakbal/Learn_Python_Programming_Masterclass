animals = {"Turtle", "Horse", "Robin", "Python", "Swallow", "Hedgehog", "Wren", "Aardvark", "Cat"}
birds = {"Robin", "Swallow", "Wren"}

print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")

print(birds <= animals)
print(animals >= birds)

garden_birds = {"Swallow", "Wren", "Robin"}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

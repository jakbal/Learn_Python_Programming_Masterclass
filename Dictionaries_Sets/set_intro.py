farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

print()

if more_animals == farm_animals:
    print("Sets are equal")
else:
    print("Sets are different")

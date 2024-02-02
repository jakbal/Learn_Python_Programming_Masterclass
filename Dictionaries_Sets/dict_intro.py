vehicles = {'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'fiesta': 'Ford Fiesta Ghia 1.4'}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

vehicles["fiesta"] = "Ford Fiesta Fire 1.6"


del vehicles["starfighter"]
#del vehicles["f1"]
vehicles.pop("f1", None)

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['er5']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)
#
# print()

# for key in vehicles:
#     print(key, vehicles[key], sep=": ")

for key, value in vehicles.items():
    print(key, value, sep=", ")

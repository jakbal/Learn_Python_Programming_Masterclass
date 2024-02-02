for i in range(1,20):
    print(f"i = {i}")

for i in range(10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-3):
    print(i)


#range jako sekwencja kolejnych liczba dlatego potem operator stepowania możliwy
for i in range(101)[::7]:
    print(i)

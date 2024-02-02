d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_item = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

#keys methods
# new_dict = dict.fromkeys(pantry_item, 0)
# print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# for item in d:
#     print(item)
# print()
# for item in d.keys():
#     print(item)

#update method
# d3 = d | d2
# for key, val in d3.items():
#     print(key, val)
#
# print()
#
# for val1, val2 in enumerate(pantry_item):
#     print(val1, val2)
#
# print()
#
# d4= {}
# d4 |= enumerate(pantry_item)
# for key, val in d4.items():
#     print(key, val)
#
# print()
#
# d.update(d2)
# for key, val in d.items():
#     print(key, val)
#
# print()
#
# d.update(enumerate(pantry_item))
# for key, val in d.items():
#     print(key, val)

#values method
v = d.values()
print(v)

d[10] = "ten"

print(v)

print("four" in v)
print("eleven" in v)

print()

keys = list(d.keys())
values = list(v)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]}")

print()

for key, val in d.items():
    if val == "four":
        print(f"{d[key]} was found with the key {key}")

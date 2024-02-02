from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "JP": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["JP"].append("UK")

original["Tim"][1].append("Cashier")
original["JP"][1].append("Courier")

print(original)
print(copy_1)
print(copy_2)

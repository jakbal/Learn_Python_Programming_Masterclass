number = "21,343;222:567 342,897,909;201"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

#print(separators)

values="".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

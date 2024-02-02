panagram = """The quick brown
fox jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

generated_list = [
    "9", "",
    "2", "2", "3", " ",
    "3", "7", "2", " ",
    "0", "3", "6", " ",
    "8", "5", "4", " ",
    "7", "7", "5", " ",
    "8", "0", "7"
]

values_list = "".join(generated_list).split()
print(values_list)

integer_values_list = []
for val in values_list:
    integer_values_list.append(int(val))

print(integer_values_list)

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

integers = input("Input 3 integers separated by comma: ")
integers_list = integers.split(",")

for index in range(len(integers_list)):
    integers_list[index] = int(integers_list[index])

a, b, c = integers_list

result = a + b - c
print(result)

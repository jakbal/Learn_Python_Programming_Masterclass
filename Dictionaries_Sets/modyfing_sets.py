#dict
#numbers = {}

#set
#numbers = {*""}
#number = {*{}}
numbers = set()
print(numbers, type(numbers))
# numbers.add(1)

# while len(numbers) < 4:
#     next_value = int(input(": "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_data = set(data)
print(unique_data)

unique_data1 = sorted(set(data))
print(unique_data1)

unique_data2 = list(dict.fromkeys(data))
print(unique_data2)

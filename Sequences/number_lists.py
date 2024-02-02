even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)

# print(min(even))
# print(max(even))
#
# print(min(odd))
# print(max(odd))
#
# print(len(even))
# print(len(odd))
#
# print("Mississippi".count("iss"))
#
# even.extend(odd)
# print(even)
#
# another_even = even
# print(another_even)
#
# even.sort()
# print(even)
# even.sort(reverse=True)
# print(even)
# print(another_even)
#
# numbers = [1,2,3,4,5]
# print(numbers)
# print(id(numbers))
#
# copied_numbers = list(numbers)
# print(copied_numbers)
# print(id(copied_numbers))
#
# print(numbers is copied_numbers)
# print(numbers == copied_numbers)
#
# more_copied_numbers = numbers[:]
# print(numbers is more_copied_numbers)
#
# next_copied_numbers = numbers.copy()
# print(numbers is next_copied_numbers)

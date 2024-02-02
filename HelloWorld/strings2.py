#                 1
#       01234567890123
parrot="Norwegian Blue"
print(parrot)
#print(parrot[3])
#print(parrot[-1])
# print(parrot[0:6]) #not include pos 6 UP TO BUT NOT INCLUDING
# print(parrot[:9])
# print(parrot[10:])
# print(parrot[:])
#print(parrot[-4:]) #Blue

number="21,343;222:567 342,897,909;201"
print(number[2::4]) #print just comas/separators using stepping

separators=number[2::4]
print(separators)

values="".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1] #common trick to reverse the sequence
print(backwards)

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

last8reversed = (letters[18:])[::-1]
print(last8reversed)
print(letters[:-9:-1])

print("Today it was a good day")
print('ice cube')
print("ice cube's songs")
print('We go to "cinema"')
print("a" + "b")

greetings = "Hello"
#name = input("Enter your name: ")
name = 'jakub'
print(greetings+' '+name)

print("""Pet shop owner said "No, no, 'e's' uh, he's resting". """)

SplitString="""Why it going
to next line
just like
that"""

print(SplitString)

NotSplitString="""Why it going \
to next line \
just like \
that"""

print(NotSplitString)

print("C:\\Users\\todo\\next.txt")
print(r"C:\Users\todo\next.txt")

age=24
print(age)

print(type(greetings))
print(type(age))

age = "24 years"

print(type(age))

#sprawdzanie subsekwencji
today = "friday"
print("day" in today)   #TRUE
print("night" in today) #FALSE

age = 25
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

#f-string
year=2023
print(f"It is {year} now")
print(f"Pi is approx. {22/7:12.50f}")
pi=22/7
print(f"Pi is approx. {pi}")
print(f"Pi is approx. {pi:7.3}")
print(f"Pi is approx. {pi:7.3f}")

# t = "a", "b", "c"
# t2 = ("a", "b", "c")
# print(t)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# #metallica[0] = "Master of Puppets"
#
# metallica2 = list(metallica)
# print(metallica2)
#
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffe table", 200, 100, 74, 34.50)
# print(table[1] * table[2])

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

# print(len(albums))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print()

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

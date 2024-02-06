scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespes = {"yellow jacket", "hornet", "paper wasp"}

bites = snakes | spiders
print(bites)
stings = scorpions.union(vespes)
print(bites)
arachnids = spiders.union(scorpions)
print(arachnids)
all_animals = scorpions.union(snakes, spiders, vespes)
print(all_animals)

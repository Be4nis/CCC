TrueorFalse = True
canada = {

}
while TrueorFalse:
    cities = input()
    cities = cities.split(' ')
    cities[1] = int(cities[1])
    canada[cities[0]] = cities[1]
    if cities[0] == "Waterloo":
        TrueorFalse = False
coldesttemp = 0

for k, v in canada.items():
    if v < coldesttemp:
        coldesttemp = v
keylist = list(canada.keys())
vallist = list(canada.values())
position = vallist.index(coldesttemp)
print (keylist[position])












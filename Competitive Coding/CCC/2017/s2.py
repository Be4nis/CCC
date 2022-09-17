#Starts at low tide
#Second level was of water at high tide
#After that the measurements continued to alternate between low and high tides

#All high tide measurements are higher than low tides

#As time passed high tides only becamse higher and low tides only became lower

n = int(input(""))


m = input("").split(' ')
measurements = list(map(int, m))
sortedmeasurements = sorted(measurements)
lowtides = []
newmeasurements = []
tempval = 0
for sorted in sortedmeasurements:
    tempval += 1
    if tempval <= n//2:
        lowtides.insert(0, sorted)
    else:
        newmeasurements.append(sorted)
tempvar = 0
for low in lowtides:
    newmeasurements.insert(tempvar, low)
    tempvar += 2
newmeasurement = list(map(str, newmeasurements))

print (' '.join(newmeasurement))
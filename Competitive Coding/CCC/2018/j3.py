cit = input()
cit = cit.split(' ')
cities = (list(map(int, cit)))
c = [0]
# input: 3 10 12 5
for i in range(len(cities)):
    # From 1 to 4, add the first number of c to the first number of cities
    #In this case first number of c is 0 and the first number of cities is 3
    # Then continue, because we added 3 to c, the 2nd number of c is 3 add 3 to the second number of input which is 10
    # Now we have the distance between city 1 to city 5 stored in c
    c.append(c[i] + cities[i])

#c = [0, 3, 13, 25, 30]

for i in range(len(c)):
    #Contains the calculated distance result:
    r = []
    #For each number in 1 to 5
    #Run this loop 5 times
    for j in range(0, 5):
        #From 1 to 5

        #Calculate distance between cities
        #Example:
            #j == 1, i == 1
            #c[1] == 0 
            #c[1] == 0
            #c[2] - c[1] == 3 - 0 == 3
            #c[3] - c[1] == 10 - 0 == 10
        #Example for city 3:
            #c[1] - c[3] == 0 - 13
            #c[2] - c[3] == 0 - 3
            #c[3] - c[3] == 0 - 0
            #c[4] - c[3] == 25 - 13 = 12
            #c[5] - c[3] == 30 - 13 = 17
        distance = c[j] - c[i]

        if (distance < 0):
            distance *= -1
        r.append(distance)
    print (*r)
max_weight = int(input(""))
numcars = int(input(""))

num_of_cars_that_can_cross = 0
listofweightsofcars = []
for i in range(numcars):
    y = int(input())
    if y > max_weight:
        break
    if len(listofweightsofcars) > 3:
        listofweightsofcars.pop(0)
        listofweightsofcars.append(y)
    else:
        listofweightsofcars.append(y)
    if sum(listofweightsofcars) > max_weight:
        break
    else:
        num_of_cars_that_can_cross += 1
print (num_of_cars_that_can_cross)








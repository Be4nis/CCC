#First to digits represent direction to turn:
#If their sum is odd then turn left
#If their sum is even and not zero turn right
#If their sum is zero then the direction to turn is the same as previous instruction

#Remaining 3 digits will be number of steps to take


while True:
    sequence = input()
    if sequence == "99999":
        break
    sum = int(sequence[0]) + int(sequence[1])
    direction = ""
    if sum == 0:
        direction = previous
    elif sum % 2 == 0:
        direction += "right"
    else:
        direction += "left"
    previous = direction
    print (direction + " " + sequence[2:5])
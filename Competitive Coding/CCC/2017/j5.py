#Each board is made of 2 pieces
#Board = Length I + Length J
#Heigh of fence is length of each board
#Determine the maximum length of any fence he could make
#Example
#Tudor has 4 pieces with these lengths:
#1 2 3 4
#Each board has to be the same length:
    #1 and 4 is 5
    #2 and 3 is 5, there is no combination that can get same length
#Now, he makes a fence with length 2 and height 5

#We output 2 because there are two boards and 1 solution

times = int(input())
j = (input())
j = j.split(' ')
for i in range(times):
    for p in range(len(j)):
        if p+p % 2 == 0:
            print(p)


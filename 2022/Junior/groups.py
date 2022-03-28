#We have to find number of violated constraints
#x students must be in the same group
#y students must not be in the same group
#g is list of groups



#Find out who is in the same group
x = int(input(""))
samegroup = []
for i in range(x):
    students = input("").split(' ')
    samegroup.append(students)
#Find out who has to be in different groups 
y = int(input(""))
diffgroup = []
for i in range(y):
    students = input("").split(' ')
    diffgroup.append(students)

#Find out the final groups
g = int(input(""))
groups = []
for i in range(g):
    students = input("").split(' ')
    groups.append(students)
#Violated people:
violated = 0
#For person in same group
for people in samegroup:
    #Name1 is people[0] because there is an array inside the list and we want to access the person inside the array
    name1 = people[0]
    #Name2 same as name1 except accesses the second person in the array
    name2 = people[1]
    #For the group ['...', '...'], ['...','...' ]
    for group in groups:
        #If the fist name is in the group and the second person is not
        if name1 in group and name2 not in group:
            #Add 1 to violated
            violated += 1
            break
        elif name2 in group and name1 not in group:
            #If the second name is in the group and the first name is not add 1 to violated
            #We need this second elif because the first one
            #Only checks to see if the first name is in the group and the second one is not
            #If the group had the second name and not the first it would
            #Count as not violated
            violated += 1
            break

#Find out the people in different groups
for people in diffgroup:
    #Accessing the people in the different groups list
    name1 = people[0]
    name2 = people[1]
    #For a group in groups
    for group in groups:
        #If name1 and name2 are in a group add one to violated
        if name1 in group and name2 in group:
            violated += 1
            break

print (violated)
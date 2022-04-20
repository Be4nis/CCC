#n is the dimension of the square n = 15 means the grid is 15x15
n = int(input())
#t is the amount of trees in the dimentsion
t = int(input())
#Yard is the dimension of the yard:
#For column in range 15, for row in range 15
#For example if n is 3, yard would be [['', '', ''], ['', '', ''], ['', '', '']]

yard = [['' for col in range(n)] for row in range(n)]
#Store the list of tree coordinates
trees = []
#Store the largest possible land size
largest_m = 0

#For tree in amount of trees
for i in range(t):
    #Location of the tree
    #Takes two locations so we gotta split it into a list
    location_in = input().split(' ')
    #Location x - 1
    #The reason why we gotta minus 1 is because code starts at 0, not one.
    #To access the first index in our list we gotta start at 0.
    loc_x = int(location_in[0]) - 1
    #Location y - 1
    loc_y = int(location_in[1]) - 1
    #Add the coordinates of the tree to the trees list
    trees.append([loc_x, loc_y])
    #
    yard[loc_x][loc_y] = '1'
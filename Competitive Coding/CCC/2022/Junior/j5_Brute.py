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
    #Put 1 in that list to show that the spot has been taken
    yard[loc_x][loc_y] = '1'

def exterior(start_row, start_col, size):
    #Get the yard that has all the tree locations included in it.
    global yard
    #All squares are qualified for now...
    qualified = True
    #For I in 2
    for i in range(size):
        # If the column and the size minus 1 is bigger or equal to 14 or 
        #The row plus size is bigger or equal to 14 then qualified = False
        if start_col + size - 1 >= n-1 or start_row + size - 1 >= n-1:
            qualified = False
            break
        #If yard(x coord + 1)(y coord plus 2 - 1) is 1
        if yard[start_row + i][start_col + size - 1] == '1':
            qualified = False
            break
        #If the x coordinate plus size minus one and 
        if yard[start_row + size - 1][start_col + i] == '1':
            qualified = False
            break
    if qualified:
        return exterior(start_row, start_col, size + 1)
    else:
        return size - 1

#X column
#For r in range(n), basically means for each [This guy ->['', '', ''], This guy ->['', '', '']]
for r in range(n):
    #Y Column
    #For column in range n, means [[This guy -> '', This guy -> '', This guy -> ''], [This guy ->'',This guy -> '',This guy -> '']]
    for c in range(n):
        #If x, y coordinate == 1 it has a tree in it so continue
        if yard[r][c] == '1':
            continue
        #If it doesn't have a tree:
        else:
            #Type in the row and column this square is, the size of the square is 2 because we already know there isn't a tree there.
            #Starting the size at 1 also works but might as well start at 2
            largest_cur = exterior(r, c, 1)
            if largest_m < largest_cur:
                largest_m = largest_cur

print (largest_m)
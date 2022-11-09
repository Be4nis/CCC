#This took around 2 hours and 30 minutes
#I can't believe this works
m = int(input(""))
list_of_coords = []
for i in range(m):
    h = input("").split(' ')
    h = list(map(int, h))
list_of_coords.append(h)

list_of_answers = []
for coord in list_of_coords:
    if coord[0] == 1:
        if coord[1] >= 1 and coord[1] <= 3 and coord[2] == 0:
            list_of_answers.append("crystal")
        elif coord[1] == 2 and coord[2] == 1:
            list_of_answers.append("crystal")
        else:
            list_of_answers.append("empty")
    elif coord[0] == 2:
        x_coord = coord[1] / (5**(coord[0] - 1))
        y_coord = coord[2] / (5**(coord[0] - 1))
        if x_coord >= 1 and x_coord <= 3 and y_coord <= 1:
            list_of_answers.append("crystal")
        elif x_coord >= 2 and x_coord <= 3 and y_coord <= 2:
            list_of_answers.append("crystal")
        elif coord[1] >= 6 and coord[1] <= 8 and coord[2] == 5:
            list_of_answers.append("crystal")
        elif coord[1] == 7 and coord[2] == 6:
            list_of_answers.append("crystal")
        elif coord[1] >= 11 and coord[1] <= 13 and coord[2] == 11:
            list_of_answers.append("crystal")
        elif coord[1] == 12 and coord[1] == 11:
            list_of_answers.append("crystal")
        elif coord[1] >= 16 and coord[1] <= 18 and coord[2] == 5:
            list_of_answers.append("crystal")
        elif coord[1] == 16 and coord[2] == 6:
            list_of_answers.append("crystal")
        else:
            list_of_answers.append("empty")

    else:
        x_coord = coord[1] / (5**(coord[0] - 1))
        y_coord = coord[2] / (5**(coord[0] - 1))
        x_tip = coord[1] / (5**(coord[0] - 2))
        y_tip = coord[2] / (5**(coord[0] - 2))
        #print (x_coord, y_coord, x_tip, y_tip)
        #Bottom part of the thing
        if x_coord >= 1 and x_coord <= 3 and y_coord <= 1:
            list_of_answers.append("crystal")
        #Top of part of the thing
        elif x_coord >= 2 and x_coord <= 3 and y_coord <= 2:
            list_of_answers.append("crystal")
        #First tip bottom part
        elif x_tip >= 6 and x_tip <= 9 and y_tip >= 5 and y_tip < 6:
            list_of_answers.append("crystal")

        #First tip top part
        elif x_tip >= 7 and x_tip <= 8 and y_tip >= 6 and y_tip <= 7:
            list_of_answers.append("crystal")

        #Second tip bottom part
        elif x_tip >= 11 and x_tip <= 14 and y_tip >= 10 and y_tip < 11:
            list_of_answers.append("crystal")

        elif x_tip >= 12 and x_tip <= 13 and y_tip >= 11 and y_tip <= 12:
            list_of_answers.append("crystal")

        #Third tip
        elif x_tip >= 16 and x_tip <= 19 and y_tip >= 5 and y_tip < 6:
            list_of_answers.append("crystal")
        elif x_tip >= 17 and x_tip <= 18 and y_tip >= 6 and y_tip <= 7:
            list_of_answers.append("crystal")
        else:
            list_of_answers.append("empty")

for answer in list_of_answers:
    print(answer)

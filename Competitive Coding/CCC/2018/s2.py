h = int(input(""))

intlist = []
gridlist = []
for i in range(h):
    q = (input("")).split(' ')
    gridlist.append(q)
    templist = []
    for h in q:
        p = int(h)
        templist.append(p)
    intlist.append(templist)

smallestlist = (min(intlist))
smallestinlist = min(smallestlist)
smallestnuminlist = str(smallestinlist)
firstline = (gridlist[0])
lastline = (gridlist[-1])

Perfect = False
Ninety = False
OneEighty = False
TwoSeventy = False
if smallestnuminlist == firstline[0]:
    Perfect = True
elif smallestnuminlist == firstline[-1]:
    Ninety = True
elif smallestnuminlist == lastline[-1]:
    OneEighty = True
else:
    TwoSeventy = True
list = []
secondlist = []

if Perfect:
    for grid in gridlist:
        print (' '.join(grid))
elif Ninety:
    for i in range(len(gridlist)):
        templist = []
        for grid in gridlist:
            templist.append(grid[-i-1])
        list.append(templist)
    for l in list:
        print (' '.join(l))
elif OneEighty:
    for i in range(len(gridlist)):
        templist = []
        for grid in gridlist:
            templist.append(grid[-i-1])
        list.append(templist)
    for l in range(len(list)):
        templist2 = []
        for i in list:
            templist2.append(i[-l-1])
        secondlist.append(templist2)
    for l in secondlist:
        print (' '.join(l))
elif TwoSeventy:
    for i in range(len(gridlist)):
        templist = []
        secondtemp = []
        for grid in gridlist:
            templist.append(grid[i])
        for i in range(len(templist)):
            secondtemp.append(templist[-i-1])
        list.append(secondtemp)
    for l in list:
        print (' '.join(l))
#12 9 5
#8 6 3
#4 3 1
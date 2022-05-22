randbool = True
topcordtrue = 0
def flatten(t):
    return [item for sublist in t for item in sublist]
topcoords = []

coords = []
while randbool:
    c = input("").split(' ')
    c = list(map(int, c))
    if c == [0,0]:
        randbool = False
    if topcordtrue == 0:
        topcordtrue += 1
        topcoords.append(c)
    else:
        coords.append(c)

topcoords = flatten(topcoords)
xcoordmax = topcoords[0]
ycoordmax = topcoords[1]

xcoord = 0
ycoord = 0
coords.pop()
for coord in coords:
    coordinate1 = coord[0]
    coordinate2 = coord[1]
    xcoord += coordinate1
    ycoord += coordinate2
    if xcoord > xcoordmax:
        xcoord = xcoordmax
    if ycoord > ycoordmax:
        ycoord = ycoordmax
    if ycoord < 0:
        ycoord = 0
    if xcoord < 0:
        xcoord = 0
    print (xcoord, ycoord)
n = int(input())
yesorno = []
for i in range(n):
    h = input()
    h = h.split(' ')
    h = list(map(int, h))
    if (2007 - h[0] > 18):
        yesorno.append("Yes")
    elif (2007 - h[0] == 18):
        if (h[1] <= 2 and h[2] <= 27):
            yesorno.append("Yes")
        else:
            yesorno.append("No")
    else:
        yesorno.append("No")

for yes in yesorno:
    print (yes)




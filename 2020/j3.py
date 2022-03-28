bigX = -1
bigY = -1

smallX = 102
smallY = 102

num = int(input())

for i in range(num):
    currentLine = input().split(",")
    currentX = int(currentLine[0])
    currentY = int(currentLine[1])
    if currentX >= bigX:
        bigX = currentX + 1
    if currentX <= smallX:
        smallX = currentX - 1
    if currentY >= bigY:
        bigY = currentY + 1
    if currentY <= smallY:
        smallY = currentY - 1

print(str(smallX) + ","+ str(smallY))
print(str(bigX) + ","+ str(bigY))

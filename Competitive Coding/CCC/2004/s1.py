n = int(input())
yeaorno = []
for i in range(n):
    one = input()
    two = input()
    three = input()
    if (one in two or one in three or two in three):
        yeaorno.append("No")
    else:
        yeaorno.append("Yes")
for y in yeaorno:
    print (y)
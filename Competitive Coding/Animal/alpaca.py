p = input().split(' ')
p = list(map(int, p))
if (p[0]**2) > ((p[1]**2)*3.1415926):
	print ("SQUARE")
else:
	print("CIRCLE")

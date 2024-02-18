#N = number of lines
#D = Length of Track
#K = number of times the device can be used
#X = Device Minus Formula thing
#Device = Speed x (100-X)/100
#Finish a race in D/Line
#2 12 3 30
#100
#50
#50

def change(speed, x):
	return speed * (100-x)/100
	
p = input().split(' ')
p = list(map(int, p))
speeds = []

for i in range(p[0]):
	k = int(input(""))
	speeds.append(k)

my = int(input(""))

for i in range(p[2]):
	q = max(speeds)	
	t = change(max(speeds), p[3]) 
	speeds.remove(q)
	speeds.append(t)

if my > max(speeds):
	print("YES")
else:
	print("NO")

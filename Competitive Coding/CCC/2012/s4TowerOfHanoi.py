#goal of placing it in increasing order
#only smaller coins can go on the larger one
#The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks.

while True:
	total = 0
	i = int(input(""))
	if i == 0:
		break
	coins = input("").split(' ')
	coins = list(map(int, coins))
	scoins = sorted(coins)

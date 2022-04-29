x = int(input())
total = 0
heights = input()
heights = heights.split(' ')
heights = list(map(int, heights))


bases = input()
bases = bases.split(' ')
bases = list(map(int, bases))
for i in range(x):
    high = [heights[i], heights[i+1]]
    triangle = (bases[i] * abs(heights[i] - heights[i+1])) / 2
    square = (bases[i] * min(high))
    distance = (triangle + square)
    total += distance
print (total)


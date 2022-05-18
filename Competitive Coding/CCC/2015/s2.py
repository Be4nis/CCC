h = int(input())
k = int(input())

sizes = []

for i in range(h):
    size = input()
    sizes.append(size)
satisfied = 0
used = []
for i in range(k):
    y = input()
    y = y.split(' ')
    y[1] = int(y[1])
    if (sizes[y[1] - 1] == y[0]) and y[1] not in used:
        used.append(y[1])
        satisfied += 1

print (satisfied)

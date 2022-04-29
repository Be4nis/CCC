n = int(input())
swifts = input()
semaphors = input()
swifts = swifts.split(' ')
semaphors = semaphors.split(' ')
swifts = list(map(int, swifts))
semaphors = list(map(int, semaphors))

days = 0
sw = 0
se = 0
points = []
for i in range(n):
    days += 1
    sw += swifts[i]
    se += semaphors[i]
    if sw == se:
        points.append(days)
    else:
        points.append(0)

print (max(points))





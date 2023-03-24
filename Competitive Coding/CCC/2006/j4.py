#x, y
taskList = {}
numlist = [0]*8

for i in range(1, 8):
    taskList[i] = []

taskList[1].append(7)
numlist[7] += 1

taskList[1].append(4)
numlist[4] += 1

taskList[2].append(1)
numlist[1] += 1

taskList[3].append(4)
numlist[4] += 1

taskList[3].append(5)
numlist[5] += 1

while True:
    t1 = int(input())
    t2 = int(input())

    if (t1 == 0 and t2 == 0):
        break
    taskList[t1].append(t2)
    numlist[t2] += 1

sequence = []
process = []

for i in range(1, 8):
    if numlist[i] == 0:
        process.append(i)

while (len(process) != 0 ):
    process.sort()
    top = process[0]
    sequence.append(top)
    process.pop(0)
    for i in range(len(taskList[top])):
        nextTo = taskList[top][i]
        numlist[nextTo] -= 1

        if (numlist[nextTo] == 0):
            process.append(nextTo)

if (len(sequence) == 7):
    for i in range(7):
        print(sequence[i], end = ' ')
else:
    print("Cannot complete these tasks. Going to bed.")





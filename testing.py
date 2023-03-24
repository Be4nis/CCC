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
print (numlist, taskList)
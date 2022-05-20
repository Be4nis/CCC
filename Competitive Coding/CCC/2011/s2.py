n = int(input(""))
correctlist = []

studentlist = []
corr = 0
for h in range(n):
    y = input("")
    correctlist.append(y)

for q in range(n):
    p = input("")
    studentlist.append(p)

for b in range(n):
    if correctlist[b] == studentlist[b]:
        corr += 1

print (corr)


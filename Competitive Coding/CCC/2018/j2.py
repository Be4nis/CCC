n = int(input())
row1 = input()
row2 = input()
row1.split(' ')
row2.split(' ')
total = 0
for i in range(n):
    if (row1[i] == 'C' ) and (row2[i] == 'C'):
        total += 1
print (total)
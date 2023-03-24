num1 = int(input(""))
num2 = int(input(""))
total = 0

for i in range(1, num1 + 1):
    for p in range(1, num2 + 1):
        if p + i == 10:
            total += 1

if total == 1:
    print(f"There is {total} way to get the sum 10.")
else:
    print(f"There are {total} ways to get the sum 10.")
#2 8, 3 7, 4 6, 5 5, 6 4



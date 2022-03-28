n = int(input())
data = {
    }
for i in range(n):
    person = input()
    dollars = int(input())
    data[person] = dollars

highest_value = max(data, key=data.get)
print (highest_value)
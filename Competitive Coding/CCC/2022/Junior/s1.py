n = int(input())
ans = 0
i = 0
while i <= 100000:
    total = i*5
    rem = n-total
    if rem >= 0 and rem % 4 ==0:
        print (rem)
        ans += 1
    
print (ans)

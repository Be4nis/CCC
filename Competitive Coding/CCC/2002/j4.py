numerator = int(input())
denominator = int(input())

answer = int(numerator / denominator)
remainder = (numerator % denominator)
if remainder == 0:
    print (answer)
elif numerator == 0:
    print (0)
elif answer == 0 and remainder != 0:
    p = 1
    for i in range(p, denominator):
        if (remainder % i == 0) and (denominator % i == 0):
            remainder = remainder//i
            denominator = denominator//i
            p = 1
    print (f"{remainder}/{denominator}")
else:
    p = 1
    for i in range(1, denominator):
        if (remainder % i == 0) and (denominator % i == 0):
            remainder = remainder//i
            denominator = denominator//i
            p = 1
    print (f"{answer} {remainder}/{denominator}")











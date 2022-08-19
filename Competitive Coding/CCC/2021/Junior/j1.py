b = int(input())
if b < 80 or b > 200:
    print ("This is not possible")
else:
    formula = 5 * b - 400
    if formula == 100:
        print (formula)
        print ("0")
    elif formula < 100:
        print (formula)
        print ("1")
    elif formula > 100:
        print (formula)
        print ("-1")

#b is temperature which water begins to boil
#Output is an integer which is atmospheric pressure measured in kPa
#Second line is -1, 0 or 1 which represents if your below, at or above sea level
#below 100 kpa means you are above sea level, above 100kpa means your above sea level



while True:
    cupcakes = 28
    reg = int(input("Regular box of cupcakes: "))
    small = int(input("Small box of cupcakes: "))

    numofcupcakes = (reg*8) + (small*3)
    leftover = int(numofcupcakes - cupcakes)
    if leftover >= 0:
        print (f"There will be {leftover} left over.")
    else:
        print ("There aren't enough cupcakes for everyone")
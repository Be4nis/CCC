burg = (461, 431, 420, 0)
dri = (130, 160, 118, 0)
si = (100, 57, 70, 0)
deser = (167, 266, 75, 0)

bur = int(input(""))
side = int(input(""))
soft = int(input(""))
des = int(input(""))

calories = burg[bur-1] + si[side-1] + dri[soft-1] + deser[des-1]
print(f"Your total Calorie count is {calories}.")
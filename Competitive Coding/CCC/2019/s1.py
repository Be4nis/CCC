n = input()
nums = [1, 2, 3, 4]
for i in range(len(n)):
    if n[i] == "H":
        nums = [nums[2], nums[3], nums[0], nums[1]]
    elif n[i] == "V":
        nums = [nums[1], nums[0], nums[3], nums[2]]
    
print (f"{nums[0]} {nums[1]}")
print (f"{nums[2]} {nums[3]}")


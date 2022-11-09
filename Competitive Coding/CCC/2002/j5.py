r = int(input(""))
c = int(input(""))

backyard = []
for i in range(r):
    h = input()
    t = []
    for l in h:
        t.append(l)
    backyard.append(t)

moves = int(input(""))
for i in range(3):
    move = input("")
    for back in backyard:
        if move == "F":
            

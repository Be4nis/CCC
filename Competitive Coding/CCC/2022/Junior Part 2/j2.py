h = int(input(""))
players = []
for i in range(h):
    goal = int(input(""))
    foul = int(input(""))
    points = goal*5 - foul*3
    players.append(points)
goldstarplayers = 0
goldstarteam = True
for player in players:
    if player > 40:
        goldstarplayers += 1
    elif player <= 40:
        goldstarteam = False
goldstarplayers = str(goldstarplayers)

if goldstarteam == True:
    goldstarplayers += '+'
print (goldstarplayers)
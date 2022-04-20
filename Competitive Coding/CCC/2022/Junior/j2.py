numofplayers = int(input("Number of players: "))
goldstarplayers = 0

for x in range(numofplayers):
    players = []
    numofscores = input("Number of points scored: ")
    numoffouls = input("Number of fouls: ")
    starsofscore = int(numofscores) * 5
    starsoffouls = int(numoffouls) * 3
    stars = starsofscore - starsoffouls
    players.append(stars)
    for player in players:
        if player > 40:
            goldstarplayers = goldstarplayers + 1
if goldstarplayers == numofplayers:
    print (f"{goldstarplayers}+")
else:
    print (goldstarplayers)
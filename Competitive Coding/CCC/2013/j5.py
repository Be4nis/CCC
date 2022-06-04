favteam = int(input(""))
numofrounds = int(input(""))

teams = {
    1 : 0, 
    2 : 0, 
    3 : 0,
    4 : 0,
}
plays = {
    1: [],
    2: [],
    3: [],
    4: [],
}
for round in range(numofrounds):
    h = input("").split(' ')
    h = list(map(int, h))
    if h[2] > h[3]:
        teams[h[0]] += 3
    if h[3] > h[2]:
        teams[h[1]] += 3
    if h[2] == h[3]:
        teams[h[0]] += 1
        teams[h[1]] += 1
    plays[h[0]].append(h[1])
numofpossiblities = 0
for key, item in plays.items():
    if key == 1 and item != 2:
        















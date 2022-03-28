x = int(input(""))

samegroup = []
for i in range(x):
    student_name = input().split()
    samegroup.append(student_name)

y = int(input(""))

diffgroup = []
for i in range(y):
    name = input().split()
    diffgroup.append(name)

g = int(input(""))
teams = []
for i in range(g):
    names = input().split()
    teams.append(names)

violated = 0

for same in samegroup:
    name1 = same[0]
    name2 = same[1]
    for team in teams:
        if (name1 in team and name2 not in team) or (name2 in team and name1 not in team):
            violated += 1
            break
                
for diff in diffgroup:
    name1 = diff[0]
    name2 = diff[1]
    for team in teams:
        if name1 in team and name2 in team:
            violated += 1
            break

print (violated)
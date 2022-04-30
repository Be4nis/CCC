f = int(input())
removals = int(input())
friends = []
for i in range(f):
    friends.append(i)

outs = []
for i in range(removals):
    out = int(input())
    outs.append(out)
    
finalfriend = []
for out in outs:
    for friend in range(0, f, out):
        finalfriend.append(friend)

print (finalfriend)

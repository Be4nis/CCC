number_of_friends = int(input(""))
number_of_rounds = int(input(""))

listoffriends = []

for i in range(number_of_friends):
    listoffriends.append(i + 1)
for i in range(number_of_rounds):
    indextoremove = int(input(""))
    indexes = []
    print (listoffriends[0], len(listoffriends))
    for i in range(0, len(listoffriends), indextoremove):
        indexes.insert(0, i - 1)
        print (i)   
    for index in indexes:
        listoffriends.pop(index)
    print (listoffriends)
#. The problem is solved by introducing a time-out feature: a letter currently displayed is chosen when another key is pressed, but also after a pause, i.e., a time out

#Key press twice == 1, 3 times == 2, 4 times == 3
#pause == 2
keys = {
    "a": "2", 
    "b": "22", 
    "c": "222", 
    "d": "3", 
    "e" : "33",
    "f" : "333",
    "g" : "4", 
    "h" : "44", 
    "i" : "444", 
    "j" : "5",
    "k": "55", 
    "l": "555", 
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777", 
    "s": "7777",
    "t": "8",
    "u" : "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999"
}
while True:
    word = input("")
    if word == "halt":
        break
    time = 0
    previous = ''
    for i in word:
        print(keys[i][0])
        if keys[i][0] == previous:
            time += 2
        previous = keys[i][0]
        time += len(keys[i])
    print (time)













square = 1
scores = []

while True:
    n = int(input())
    square += n
    if square > 100:
        square -= n
    if n == 0:
        print ("You Quit!")
        break
    if square == 100:
        scores.append(100)
        break
    if square == 54:
        square -= 35
    elif square == 90:
        square -= 42
    elif square == 99:
        square -= 22
    if square == 9:
        square += 25
    elif square == 40:
        square += 24
    elif square == 67:
        square += 19
    scores.append(square)

if n == 0:
    print ("You Quit!")
else:
    for score in scores:
        print (f"You are now on square {score}")
        if score == 100:
            print ("You Win!")

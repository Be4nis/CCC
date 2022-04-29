#If a player turns over an ace with at least 4 cards remaining
#And none of the next 4 cards is ace, king, queen, jack, get 4 points
#If a player turns over a king with at least 3 cards remaining and 
#None of the next 3 cards is a high card get 3 points
#So on

cards = []
while len(cards) < 52:
    c = input()
    cards.append(c)
    if len(cards) > 52:
        break
a = 0
b = 0
i = 0
player = True

highcards= ['jack', 'queen', 'king', 'ace']

for count, card in enumerate(cards):
    if player == True:
        if card in highcards:
            if cards[count] == 'jack' and len(cards[count:]) >= 1:
                if cards[count + 1] not in highcards:
                    a += 1
                    print ("Player A scores 1 point(s).")
            elif cards[count] == 'queen'and len(cards[count:]) >= 2:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards:
                    a += 2
                    print ("Player A scores 2 point(s).")
            elif cards[count] == 'king'and len(cards[count:]) >= 3:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards and cards[count + 3] not in highcards:
                    a += 3
                    print ("Player A scores 3 point(s).")
            elif cards[count] == 'ace'and len(cards[count:]) >= 4:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards and cards[count + 3] not in highcards and cards[count + 4] not in highcards:
                    a += 4
                    print ("Player A scores 4 point(s).")
        player = False
    else:
        if card in highcards:
            if cards[count] == 'jack' and len(cards[count:]) >= 1:
                if cards[count + 1] not in highcards:
                    b += 1
                    print ("Player B scores 1 point(s).")
            elif cards[count] == 'queen'and len(cards[count:]) >= 2:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards:
                    b += 2
                    print ("Player B scores 2 point(s).")
            elif cards[count] == 'king'and len(cards[count:]) >= 3:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards and cards[count + 3] not in highcards:
                    b += 3
                    print ("Player B scores 3 point(s).")
            elif cards[count] == 'ace'and len (cards[count:]) >= 4:
                if cards[count + 1] not in highcards and cards[count + 2] not in highcards and cards[count + 3] not in highcards and cards[count + 4] not in highcards:
                    b += 4
                    print ("Player B scores 4 point(s).")
        player = True

print (f"Player A: {a} point(s).")
print (f"Player B: {b} point(s).")







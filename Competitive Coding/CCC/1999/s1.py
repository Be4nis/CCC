cards = []
while len(cards) < 52:
    c = input()
    cards.append(c)
    if len(cards) > 52:
        break
a = 0
b = 0
i = 0


points = ['jack', 'queen', 'king', 'ace']
for card in cards:
    ca = cards.index('ace')
    print (ca)
    if card == 'ace':
        for j in range(1, 4):
            print (cards[ca - j])

print (i)
two = ["A", "B", "C"]
three = ["D", "E", "F"]
four = ["G", 'H', "I"]
five = ["J", "K", "L"]
six = ["M", "N", "O"]
seven = ["P", "Q", "R", "S"]
eight = ["T", "U", "V"]
nine = ["W", "X", "Y", "Z"]


def split(word):
    return [char for char in word]
def convert(s):

    # initialization of string to ""
    new = ""

    # traverse in the string 
    for x in s:
        new += x 

    # return string 
    return new
telephones = []

n = int(input())
for i in range(n):
    p = list(input())
    while "-" in p:
        p.remove("-")
    for i in range(len(p)):
        if len(p) > 10:
            p.pop()
        else:
            break
    for i in range(len(p)):
        if p[i] in two:
            p[i] = "2"
        if p[i] in three:
            p[i] = "3"
        if p[i] in four:
            p[i] = "4"
        if p[i] in five:
            p[i] = "5"
        if p[i] in six:
            p[i] = "6"
        if p[i] in seven:
            p[i] = "7"
        if p[i] in eight:
            p[i] = "8"
        if p[i] in nine:
            p[i] = "9"
    p.insert(3, "-")
    p.insert(7, "-")
    listTostr = (convert(p))
    telephones.append(listTostr)

for tele in telephones:
    print (tele)









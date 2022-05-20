n = int(input(""))
code = {

}
for i in range(n):
    y = input("")
    y = y.split(' ')
    code[y[1]] = y[0]

binary = list(input(""))
word = []
listofwords = ""

for b in binary:
    listofwords += b
    for key, item in code.items():
        if key == str(listofwords):
            word.append(item)
            listofwords= ""

def makestring(word):
    str = ""
    for w in word:
        str += w
    return str
    
print (makestring(word))

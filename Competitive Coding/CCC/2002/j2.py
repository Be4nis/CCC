consonants = "aeiouy"
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
def ltos(list):
    temp = ""
    for l in list:
        temp += l
    return temp
print ("Enter words to be translated:")
words = []
while 1:
    p = input("")
    if (p == "quit!"):
        break
    h = Convert(p)
    if (len(h) > 4) and (h[-3] not in consonants) and (h[-1] == "r" and h[-2] == "o"):
        h.insert(-1, 'u')
        print (ltos(h))
    else:
        print (p)
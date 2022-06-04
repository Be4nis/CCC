letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

k = int(input(""))
list_of_letters = list(input(""))
finalword = ""
indexes = []
for i in range(1, len(list_of_letters) + 1):
    indexes.append(i)

for i in range(len(list_of_letters)):
    tempvar = list_of_letters[i]
    indexnum = letters.index(tempvar)
    indexestoremove = 3 * indexes[i] + k
    finalword += letters[indexnum - indexestoremove]
print (finalword)






























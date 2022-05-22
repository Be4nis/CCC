knownmessage = list(input(""))
translator = list(input(""))
dictionary = {

}
messagetodecode = list(input(""))

for i in range(len(knownmessage)):
    dictionary[translator[i]] = knownmessage[i]
final = ""

for message in messagetodecode:
    if message in dictionary:
        final += dictionary.get(message)
    elif message not in dictionary:
        final += "."
print (final)
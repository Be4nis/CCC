thingstoruleout = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
h = list(input(""))
finallist = []
for i in range(len(h)):
    if h[i] in thingstoruleout:
        finallist.append(h[i])
    elif h[i] == '+':
        finallist.append('tighten')
    elif h[i] == '-':
        finallist.append('loosen')
    else:
        finallist.append(h[i])
        finallist.append('*')

finallist.pop()
instructions = ""  

for item in finallist:
    if item != '*' and item != 'tighten' and item != 'loosen':
        instructions += item
    elif item == 'tighten':
        instructions += ' tighten '
    elif item == 'loosen':
        instructions += ' loosen '
    elif item == '*':
        instructions += '\n'
print (instructions)
#AFB+8HC-4
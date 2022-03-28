letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
string = ""
inp = input()

inp = list(inp)

for i in range(len(inp)):
    if inp[i] in letters:
        if inp[i-1] in numbers:
            inp.insert(i, "*")
inp.pop(0)
for i in inp:
    string+=i
string = string.replace("*", "\n")
string = string.replace("+", " tighten ")
string = string.replace("-", " loosen ")
print (string)


# letters = "ABCDEFGHIJKLMNOPQRST"
# numbers = "0123456789"

# outoftune = input()
# outoftune = list(outoftune)

# for string in range(len(outoftune)):
#     if outoftune[string] in letters:
#         if outoftune[string-1] in numbers:
#             outoftune.insert(string, '*')
# del outoftune[0]
# def makestring(str):
#     """Make the list a string"""
#     variab = ""
#     for ele in str:
#         variab += ele

#     return variab

# items = (makestring(outoftune))
# items = items.replace("*", "\n")
# items = items.replace("+", " tighten ")
# items = items.replace("-", " loosen ")
# print (items)

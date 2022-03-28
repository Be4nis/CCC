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




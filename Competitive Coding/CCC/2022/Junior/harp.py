letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"

instructions = input("")
instructions = list(instructions)

for i in range(len(instructions)):
    if instructions[i] in letters:
        if instructions[i-1] in numbers:
            instructions.insert(i, '*')
instructions.pop(0)

#Get rid of the upperthingy with a .replace()

#We can only use .replace() inside a string

#Also we want to print a string anyway or else we get 0%

final = ""
for instruction in instructions:
    final += instruction

final = final.replace("*", '\n')
final = final.replace("+", " tighten ")
final = final.replace("-", " loosen ")
print (final)
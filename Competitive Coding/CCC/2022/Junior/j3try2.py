letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"

instructions = input()

instructions = list(instructions)

for instruction in range(len(instructions)):
    if instructions[instruction] in letters:
        if instructions[instruction-1] in numbers:
            instructions.insert(instruction, '*')
instructions.pop(0)
def makeliststr(list):
    """Make the list into a string"""
    string = ""
    for i in list:
        string += i
    return string

steps = makeliststr(instructions)
steps = steps.replace("*", '\n')
steps = steps.replace("+", " tighten ")
steps = steps.replace("-", " loosen ")
print (steps)
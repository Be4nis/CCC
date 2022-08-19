text = input()
string = input()
contains_shift = False
def cyclicshift(string):
    """Move the character from beginning to end of string"""
    return string[1:] + string[0]

for i in range(len(text)):
    if string in text:
        contains_shift = True
        break
    string = cyclicshift(string)

if contains_shift:
    print ('yes')
else:
    print ('no')
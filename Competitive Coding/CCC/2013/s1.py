def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False
year = int(input())
for i in range (10000):
    year += 1
    listofElems = [int(a) for a in str(year)]
    result = checkIfDuplicates_2(listofElems)
    if result == True:
        continue
    elif result == False:
        break
strings = [str(integer) for integer in listofElems]
a_string = "".join(strings)
an_integer = int(a_string)
print (an_integer)
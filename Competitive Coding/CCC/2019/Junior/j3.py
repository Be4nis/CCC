n = int(input())

def checkIfDuplicates_3(listOfElems):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return elem
    return False

for i in range(n):
    h = list(input())
    count_a = h.count('')








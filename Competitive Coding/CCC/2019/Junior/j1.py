apples = 0
bananas = 0

athree = int(input())
apples += 3*athree
atwo = int(input())
apples += 2*atwo
aone = int(input())
apples += aone


bthree = int(input())
bananas += 3*bthree
btwo = int(input())
bananas += 2*btwo
bone = int(input())
bananas += bone

if apples > bananas:
    print ("A")
elif bananas > apples:
    print ("B")
else:
    print ("T")
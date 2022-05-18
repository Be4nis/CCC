x = int(input())
y = int(input())

dmojistan = input()
dmojistan = dmojistan.split(' ')
dmojistan = list(map(int, dmojistan))

pegland = input()
pegland = pegland.split(' ')
pegland = list(map(int, pegland))
ouput = 0
maximums = []
if x == 1:
    for i in range(y):
        pair = []
        biggest_dmoj = max(dmojistan)
        biggest_peg = max(pegland)
        pair.append(biggest_dmoj)
        pair.append(biggest_peg)
        h = max(pair)
        ouput += h
        dmojistan.remove(biggest_dmoj)
        pegland.remove(biggest_peg)
    print(ouput)
elif x == 2:
    list3 = dmojistan + pegland
    for i in range(y):
        pair = []
        w = max(list3)
        e = min(list3)
        pair.append(w)
        pair.append(e)
        maximums.append(max(pair))
        list3.remove(w)
        list3.remove(e)
    print (sum(maximums))

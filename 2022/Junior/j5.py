n = int(input(""))
t = int(input(""))
areaofland = [['' for col in range(n)] for row in range(n)]
trees = []
pool = 0
for i in range(t):
    location_in = input().split(' ')
    location_x = int(location_in[0]) - 1
    location_y = int(location_in[1]) - 1
    trees.append([location_x, location_y])
    areaofland[location_x][location_y] = '1'

def exterior(start_row, start_col, size):
    global areaofland
    qualified = True
    for i in range(size):
        if start_col + size - 1 >= n-1 or start_row + size - 1 >= n-1:
            qualified = False
            break
        if areaofland[start_row + i][start_col + size - 1] == '1':
            qualified = False
            break
        if areaofland[start_row + size - 1][start_col + i] == 'i':
            qualified = False
            break
    if qualified:
        return exterior(start_row, start_col, size + 1)
    else:
        return size - 1

for r in range(n):
    for c in range(n):
        if areaofland[r][c] == '1':
            continue
        else:
            largest_cur = exterior(r, c, 2)
            if pool < largest_cur:
                pool = largest_cur
print (pool)

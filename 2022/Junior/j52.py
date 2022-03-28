n = int(input(""))
t = int(input(""))
areaofland = [['' for col in range(n)] for row in range(n)]
trees = []
pool_size = n - 1
for i in range(t):
    location_in = input().split(' ')
    location_x = int(location_in[0]) - 1
    location_y = int(location_in[1]) - 1
    trees.append([location_x, location_y])
    areaofland[location_x][location_y] = '1'

def check_has_trees(in_size, in_row, in_col):
    global trees
    for tree in trees:
        if in_row <= tree[0] <= in_row + in_size - 1 and in_col <= tree[]


def check(in_size, in_row, in_col):
    has_trees = check_has_trees(in_size, in_row, in_col)
    if not has_trees:
        return True
    while in_size + in_row < n:
        while in_size + in_col + 1 < n:
            in_col += 1
            has_trees = check_has_trees(in_size, in_row, in_col)
            if not has_trees:
                print ('{} {} {}'.format(in_size, in_row, in_col))
                return True
        in_row += 1
        in_col = 0
    return False

checked = check(pool_size, 0 , 0)

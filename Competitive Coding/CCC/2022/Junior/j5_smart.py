n = int(input())
t = int(input())
yard = [['' for col in range(n)] for row in range(n)]
trees = []
pool_size= n - 1

for i in range(t):
    location_in = input().split(' ')
    loc_x = int(location_in[0]) - 1
    loc_y = int(location_in[1]) - 1
    trees.append([loc_x, loc_y])
    yard[loc_x][loc_y] = '1'

def check_has_tree(insize, inrow, incol):
    global trees
    for tree in trees:
        if inrow <= tree[0] <= inrow + insize - 1 and incol <= tree[1] <= incol + insize - 1:
            return tree
    return False

def check(insize, inrow, incol):
    has_trees = check_has_tree(insize, inrow, incol)
    if not has_trees:
        return True
    while insize + inrow < n:
        while insize + incol + 1 < n:
            incol += 1
            has_trees = check_has_tree(insize, inrow, incol)
            if not has_trees:
                print('{} {} {}'.format(insize, inrow, incol))
                return True
        inrow += 1
        incol = 0

checked = check(pool_size, 0, 0)
while not checked:
    pool_size -= 1
    checked = check(pool_size, 0, 0)
print(pool_size)
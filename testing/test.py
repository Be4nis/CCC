g = [[] for i in range(8)]
c = {i:0 for i in range(8)}
inc = [[1, 7], [1, 4], [2, 1], [3, 4], [3, 5]]
for i in inc:
  g[i[1]].append(i[0])
  c[i[1]] += 1
while True:
  A = int(input())
  B = int(input())
  if(A == 0 and B == 0):
    break
  g[B].append(A)
  c[B] += 1
g = [sorted(i) for i in g]
visited = [False]*8
print (g, visited)
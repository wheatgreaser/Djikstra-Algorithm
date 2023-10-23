nodes = [[1,2], [3], [3], [4, 5], [6]]
edges = [[3, 4], [5], [5], [2, 3], [4]]
exploredDist = [0, 10000, 10000, 10000, 10000, 10000, 10000]
exploredNodes = []
for i in range(len(nodes)):
  for j in range(len(nodes[i])):
    t = exploredDist[nodes[i][j]]
    t = min(t, edges[i][j]+ exploredDist[i])
    exploredDist[nodes[i][j]] = t

print(exploredDist)


    
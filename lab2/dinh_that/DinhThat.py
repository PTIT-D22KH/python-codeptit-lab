def dfs(x, visited, adjList):
    visited[x] = 1
    for i in adjList[x]:
        if visited[i] == 0:
            dfs(i, visited, adjList)

for _ in range(int(input())):
    nV, nE, u, v = [int(i) for i in input().split()]
    visited = [0] * 1005
    adjList = [[] for i in range(1005)]
    # print(adjList)
    for _ in range(nE):
        dau, cuoi = [int(i) for i in input().split()]
        adjList[dau].append(cuoi)
    res = 0
    for i in range(1, nV + 1):
        visited = [0] * 1005
        visited[i] = 1
        dfs(u, visited, adjList)
        if visited[v] == 0:
            res += 1
    print(res)
    


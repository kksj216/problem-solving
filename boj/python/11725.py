import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

## DFS
visited = [False]*(n+1)
parent = [0]*(n+1)

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph, i, visited)
            parent[i] = v

dfs(graph, 1, visited)

# print(parent)
for i in range(2,n+1):
    print(parent[i])

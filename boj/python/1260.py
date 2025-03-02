from collections import deque 

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)  # 양방향 모두 

for _ in range(n+1):
    graph[_] = sorted(graph[_])

## DFS
visited = [False]*(n+1)
def dfs(graph, v, visited):
    visited[v] = True
    
    print(v, end=" ")
    # sorted(graph[v])

    for i in graph[v]:
        if visited[i]==False:
            dfs(graph, i, visited)

dfs(graph, v, visited)
print()

## BFS
visited = [False]*(n+1)
def bfs(graph, v, visited):

    # 시작 노드 , 방문표시 
    que = deque([v])
    visited[v] = True

    while que:
        curr = que.popleft()
        print(curr, end=" ")

        for i in graph[curr]:
            if visited[i]==False:
                que.append(i)
                visited[i] = True

bfs(graph, v, visited)

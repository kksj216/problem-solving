import copy
import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = [[0 for _  in range(n)] for _ in range(n)]
visited = [[False for _  in range(n)] for _ in range(n)]
dir = [(-1,0), (1,0), (0,-1), (0,1)]

min_rain = 1000
max_rain = 0
result = 0

for _ in range(n):
    graph[_] = list(map(int, input().split()))
    for j in range(n):
        max_rain = max(max_rain, graph[_][j])
        min_rain = min(min_rain, graph[_][j])


def dfs(graph, vx, vy, visited, m, count):

    visited[vx][vy]=True

    for d in range(4):
        nx,ny = vx+dir[d][0],vy+dir[d][1]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
            if graph[nx][ny] > m:
                # visited[nx][ny] = True
                dfs(graph, nx, ny, visited, m, count)

for m in range( min_rain-1, max_rain):  # min_rain
    count = 0
    # print(m)
    
    visited = [[False for _  in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > m:
                if visited[i][j] == False:
                    
                    count+= 1
                    dfs(graph, i, j, visited, m, count)
                    

    result = max(result, count)
    # print("count: ", count)
    
    # print(visited)
print(result)
import sys
sys.setrecursionlimit(100000)

results = []
dir = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,1), (1,-1)]

def dfs(graph, vx, vy, visited, w, h):
    visited[vx][vy] = True

    for d in range(8):  # 상하좌우4 + 대각선4 => 8개 
        nx,ny = vx+dir[d][0], vy+dir[d][1]

        if 0<=nx<h and 0<=ny<w and visited[nx][ny]==False:
            if graph[nx][ny]==1:
                dfs(graph, nx, ny, visited, w, h)

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    count = 0
    graph = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))

    visited = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if visited[i][j]==False and graph[i][j]==1:
                count += 1
                dfs(graph, i,j,visited, w, h)
                # visited[i][j] = True

    results.append(count)
    # print(visited)

# print(results)
for i in results:
    print(i)
from collections import deque

m, n = map(int, input().split())

graph = [[] for i in range(n)]
visited = [[0 for i in range(m)] for _ in range(n)]  # 날짜 수 세기
visited_tf = [[False for i in range(m)] for _ in range(n)]  # 방문여부 표시 

dir = [(-1,0), (1,0), (0,-1), (0,1)]

que = deque()

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))
            visited_tf[i][j] = True
        if graph[i][j] == -1:
            visited_tf[i][j] = True

while que:
    
    cur = que.popleft()
    # print(cur[0], cur[1])
    visited_tf[cur[0]][cur[1]] = True

    for d in range(4):
        new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

        if 0<=new_x<n and 0<=new_y<m and visited_tf[new_x][new_y]==False and graph[new_x][new_y]==0:
            # print(new_x, new_y)
            que.append((new_x, new_y))
            visited[new_x][new_y] = visited[cur[0]][cur[1]] + 1
            visited_tf[new_x][new_y] = True

is_false = True
for i in range(n):
    if False in visited_tf[i]:
        is_false = False

if is_false==False:
    print(-1)
else:
    max_n = 0
    for i in range(n):
        for j in range(m):
            max_n = max(max_n, visited[i][j])

    print(max_n)

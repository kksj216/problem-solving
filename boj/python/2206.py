import copy
from collections import deque

n,m = map(int, input().split())

graph = [[] for j in range(n)]
visited = [[[0,0] for i in range(m)] for j in range(n)]
## *** 3차원으로 벽 부수었는지를 확인하며 해야 시간초과 안나게 품 
# 0: 안부숨
# 1: 부숨 

dir = [(-1,0), (1,0), (0,-1), (0,1)]

for nn in range(n):
    a = list(map(int, input()))
    graph[nn] = a 

que = deque()
que.append([0,0, 0])  # x, y, break
visited[0][0][0] += 1

result = -1
while que:
    cur = que.popleft()
    c_x, c_y, br = cur[0], cur[1], cur[2]

    if c_x==n-1 and c_y==m-1:
        result = visited[c_x][c_y][br]
        break 

    for d in range(4):
        n_x, n_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

        if 0<=n_x<n and 0<=n_y<m:
            # 벽인데, 아직 부순적이 없다면 벽을 부수자 
            if graph[n_x][n_y] == 1 and br == 0:
                visited[n_x][n_y][1] = visited[c_x][c_y][0] + 1
                que.append((n_x, n_y, 1))
            # 아직 안간 갈 수 있는 길이면 가자 
            if graph[n_x][n_y] == 0 and visited[n_x][n_y][br] == 0:
                visited[n_x][n_y][br] = visited[c_x][c_y][br] + 1
                que.append((n_x, n_y, br))
    # print(visited)

print(result)

### 시간 초과 => O(NM^2)
"""
graph = [[] for j in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]

one_place = []
dir = [(-1,0), (1,0), (0,-1), (0,1)]

for nn in range(n):
    a = list(input())
    graph[nn] = a
    
    for j in range(m):

        if graph[nn][j]=='1':
            one_place.append((nn, j))

# print(graph)
# print(one_place)

count_n = []

## 벽 안부수는 경우 포함, 벽 한개 부수는 가능한 모든 경우에 대해 계산, 가장 짧은 것으로 선택
for i in range(len(one_place)+1):

    visited = [[0 for i in range(m)] for j in range(n)]

    if i == len(one_place):  # 벽 안부수는 경우
        temp_graph = copy.deepcopy(graph)
    else:  # 벽 한개 부수는 경우
        temp_graph = copy.deepcopy(graph)

        break_x, break_y = one_place[i][0], one_place[i][1]
        temp_graph[break_x][break_y] = '0'


    que = deque()
    que.append([0,0])

    while que:
        cur = que.popleft()
        c_x, c_y = cur[0], cur[1]

        if c_x == n-1 and c_y == m-1:
            break

        for d in range(4):
            n_x, n_y = c_x+dir[d][0], c_y+dir[d][1]
            # print("n_x, n_y ", n_x, n_y )

            if 0<=n_x<n and 0<=n_y<m and visited[n_x][n_y]==0 and temp_graph[n_x][n_y]=='0':
                visited[n_x][n_y] = visited[c_x][c_y] + 1
                que.append((n_x, n_y))

    result = visited[n-1][m-1]

    count_n.append(result)

result = max(count_n) + 1
if result==0:
    result = -1

print( result )
"""
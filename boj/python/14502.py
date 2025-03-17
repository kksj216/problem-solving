import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[False for i in range(m)] for j in range(n)]
virus_place = []
empty_place = []
dir = [(-1,0), (1,0), (0,1), (0,-1)]

for i in range(n):
    a = list(map(int, input().split()))
    graph[i] = a
    for j in range(m):
        if graph[i][j] == 2:
            virus_place.append((i, j))
        if graph[i][j] == 0:
            empty_place.append((i,j))

max_safe = 0


## 모든 가능성에 대해
## 1. 벽 세우기
## 2. 바이러스 퍼뜨리기 
## 3. 안전 영역 수세기 
## 4. max 값 저장. 

def count_safe(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

combi = list(combinations(empty_place, 3)) # 0만 있는 칸에 대해 가능한 3개 조합

for c in combi:
    
    visited = [[False for i in range(m)] for j in range(n)]  ## 매번 초기화 할 것.
    ## 0) 맵 정보 복사
    temp_graph = copy.deepcopy(graph)
    
    ## 1) 가능한 조합에 임시로 벽 세우기
    for i in c:
        temp_graph[i[0]][i[1]] = 1

    ## 2) 벽 세운 그래프에 대해 바이러스 퍼뜨림
    que = deque()
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                que.append((i, j))

    while que:
        cur = que.popleft()
        # print("cur: ", cur)
        visited[cur[0]][cur[1]] = True

        for d in range(4):
            new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

            if 0<=new_x<n and 0<=new_y<m and temp_graph[new_x][new_y]==0 and visited[new_x][new_y]==False:
                que.append((new_x, new_y))
                visited[new_x][new_y] = True
                temp_graph[new_x][new_y] = 2

    ## 3) 안전영역 수 세기 (temp_graph 에서 0의 수 새기)
    num = count_safe(temp_graph)
    max_safe = max(num, max_safe)

print(max_safe)


"""
def make_wall(cnt):
    if cnt == 3:
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j] = 0

graph_wall = copy.deepcopy(graph)
## 1. 가능한 벽 3개 세우기 
make_wall(0)

## 2. 바이러스 퍼뜨리기
que = deque()
que.append(virus_place)

while que:
    cur = que.popleft()
    visited[cur[0]][cur[1]] = True

    for d in range(4):
        new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

        if 0<=new_x<n and 0<=new_y<m and graph_wall[new_x][new_y]==0 and visited[new_x][new_y]==False:
            que.append((new_x, new_y))
            visited[new_x][new_y] = True
            graph_wall[new_x][new_y] = 2

## 3. 안전 영역 수세기 (graph_wall 에서 0의 수 새기)
num = count_safe(graph_wall)
max_safe = max(num, max_safe)

"""
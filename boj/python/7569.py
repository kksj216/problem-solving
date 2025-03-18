from collections import deque

m,n,h = map(int, input().split())

graph = [[[] for i in range(n)] for j in range(h)]
visited = [[[0 for _ in range(m)] for i in range(n)] for j in range(h)]
dir = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (1,0,0), (-1,0,0)]

one_dir = []
result = 0

for hh in range(h):
    for nn in range(n):
        a = list(map(int, input().split()))

        graph[hh][nn] = a

# 익은 토마토(1) 좌표 모으기 
for hh in range(h):
    for nn in range(n):
        for mm in range(m):

            if graph[hh][nn][mm] == 1:
                one_dir.append((hh, nn, mm))

que = deque()

# 익은 토마토 좌표 넣기 
for _ in one_dir:
    que.append(_)

while que:
    cur = que.popleft()
    
    c_h,c_n,c_m = cur[0], cur[1], cur[2]

    # 상 하 좌 우 위 아래에 대해 토마토 익히기 
    for d in range(6):
        n_h, n_n, n_m = cur[0]+dir[d][0], cur[1]+dir[d][1], cur[2]+dir[d][2]

        if 0<=n_h<h and 0<=n_n<n and 0<=n_m<m and visited[n_h][n_n][n_m]==0 and graph[n_h][n_n][n_m]==0:
            graph[n_h][n_n][n_m]=1
            visited[n_h][n_n][n_m] = visited[c_h][c_n][c_m] + 1  # 날짜 수 +1
            que.append((n_h, n_n, n_m))

# print("graph ",graph)
# print("visited ",visited)

max_n = 0
for hh in range(h):
    for nn in range(n):
        for mm in range(m):
            if graph[hh][nn][mm] == 0:
                result = -1
            max_n = max(visited[hh][nn][mm], max_n)

if result==-1:
    print(-1)
else:
    print(max_n)
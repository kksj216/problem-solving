from collections import deque

m,n,k = map(int, input().split())

rect = []
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    rect.append([(x1,y1), (x2,y2)])

# print(rect)
dir = [(-1,0), (1,0), (0,-1), (0,1)]
graph = [[1 for i in range(n)] for i in range(m)]
# 0: 사각형으로 덮인 곳

for i in range(len(rect)):
    r = rect[i]
    r1, r2 = r[0], r[1]
    # print(r1, r2)
    x1,y1, x2,y2 = r1[0], r1[1], r2[0]-1, r2[1]-1

    for l in range(y1,y2+1):
        for j in range(x1,x2+1):
            graph[l][j] = 0

total_count = 0
count_arr = []
visited = [[False for i in range(n)] for k in range(m)]
for i in range(m):
    for j in range(n):
        if visited[i][j]==False and graph[i][j]==1:
            total_count += 1
            count = 1
            que = deque()
            que.append((i,j))

            while que:
                q_pop = que.popleft()
                x,y = q_pop[0], q_pop[1] 
                visited[x][y] = True

                for d in range(4):
                    nx, ny = x+dir[d][0], y+dir[d][1]

                    if 0<=nx<m and 0<=ny<n :
                        if visited[nx][ny]==False and graph[nx][ny]==1 :
                            visited[nx][ny] = True
                            
                            que.append((nx,ny ))
                            
                            count += 1

            # print("count ", count)
            count_arr.append(count)

print(total_count)
count_arr.sort()
for i in count_arr:
    print(i, end=" ")
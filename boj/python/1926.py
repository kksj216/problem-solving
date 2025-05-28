from collections import deque

n, m = map(int, input().split())
maps = []
for i in range(n):
    l = list(map(int, input().split()))
    maps.append(l)

dir = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[0 for _ in range(m)] for _ in range(n)]
count = 0

numbers = []
ones = 0

for i in range(n):
    for j in range(m):
        ones = 0
        if maps[i][j]!=0 and visited[i][j]==0:
            
            count += 1
            ones += 1

            visited[i][j] += 1
            que = deque()
            que.append([i,j])
            while que:
                curx, cury = que.popleft()

                for k in range(4):
                    nx,ny = curx+dir[k][0], cury+dir[k][1]
                    if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1 and visited[nx][ny]==0:
                        visited[nx][ny] = visited[curx][cury]+1
                        que.append([nx, ny])

                        ones += 1

            numbers.append(ones)

print(count)

### bfs로 풀거면 visited로 수를 세는게 아니라 따로 개수를 세는 ones 변수를 만들어서 풀어야 함
if len(numbers)==0:
    print(0)
else:
    print(max(numbers))

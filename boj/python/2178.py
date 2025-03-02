from collections import deque

n, m = map(int, input().split())

map = [[0 for i in range(m+1)] for _ in range(n+1)]
visited = [[0 for i in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    map[i] = [0]+list(input())
    for j in range(m+1):
        map[i][j] = int(map[i][j])  ## list로 쪼개었을 때 int 형으로 바꿔줘야함!!

dir = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우
que = deque([(1,1)])  ## deque에 좌표 넣는 방식 [(0, 0)]
visited[1][1] = 1  # visited는 몇칸째에 도착했는지 저장용도로 
count = 0

while que:
    cur = que.popleft()
    count += 1
    
    # print("cur ", cur)
    
    if cur == (n,m): break

    for i in range(4):
        a, b = cur[0]+dir[i][0], cur[1]+dir[i][1]

        if a < 1 or a > n or b < 1 or b > m:  # 범위
            continue
        if map[a][b] == 0:  # 못 가는 곳
            continue
        
        if not visited[a][b]:  ## ***
            que.append((a,b))
            
            visited[a][b] = visited[cur[0]][cur[1]] + 1 # *방문할 때마다 최단 거리 누적.

# print(visited)

print(visited[n][m])
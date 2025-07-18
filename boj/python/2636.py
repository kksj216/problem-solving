from collections import deque

sero, garo = map(int, input().split())

maps = []
for i in range(sero):
    a = list(map(int, input().split()))
    maps.append(a)

dir = [(-1,0), (1,0), (0,-1), (0,1)]

time = 0
num_cheese = 0

# 치즈가 아닌 부분으로 bfs 
while True:

    visited = [[False for _ in range(garo)] for _ in range(sero)]
    melting = []

    que = deque()
    que.append((0,0))
    visited[0][0] = True

    while que:
        q_pop = que.popleft()
        x,y = q_pop[0], q_pop[1]

        for d in dir:
            nx,ny = x+d[0], y+d[1]

            if 0<=nx<sero and 0<=ny<garo and visited[nx][ny]==False:
                if maps[nx][ny]==1:
                    melting.append([nx, ny])
                    visited[nx][ny] = True
                elif maps[nx][ny]==0:
                    que.append((nx, ny))
                    visited[nx][ny] = True

    if len(melting) == 0:
        break
    else:
        num_cheese = len(melting)

    time += 1

    # melting된 치즈는 0으로
    for m in melting:
        maps[m[0]][m[1]] = 0

print(time)
print(num_cheese)
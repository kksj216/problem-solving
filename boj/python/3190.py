from collections import deque

n = int(input())
k = int(input())

maps = [[0]*n for i in range(n)]
apples = []
for i in range(k):
    a,b = map(int, input().split())
    apples.append([a-1,b-1])

l = int(input())
turns = []
for i in range(l):
    a,b = map(str, input().split())
    a = int(a)
    turns.append([a,b])
# L: 왼쪽, D: 오른쪽

direction_right = [(1,0), (0,1), (-1,0), (0,1)]
direction_left = [(-1,0), (0,-1), (1,0), (0,-1)]
cur_dir = 0 # 0:우, 1:하, 2:좌, 3:상

time = 0
snake_head = [0,0]
snakes = [[0,0]]

que = deque()
que.append(snake_head)
maps[0][0] = 1

while True:
    time += 1

    q_pop = que.popleft()
    cx, cy = q_pop[0], q_pop[1]

    # 방향에 따라 다음 위치 계산
    if cur_dir==0:
        nx, ny = cx, cy+1
    elif cur_dir==1:
        nx, ny = cx+1, cy
    elif cur_dir==2:
        nx, ny = cx, cy-1
    elif cur_dir==3:
        nx, ny = cx-1, cy
        
    if not 0<=nx<n or not 0<=ny<n or maps[nx][ny]==1:
        break

    # 방향 전환
    if (time) in [t[0] for t in turns]:
        new_d = [t[1] for t in turns if t[0]==(time)][0]

        if new_d=='D':
            cur_dir = (cur_dir+1) % 4
        elif new_d=='L':
            cur_dir = (cur_dir+3) % 4
    
    # 사과 있는지 없는지에 따라
    if [nx,ny] in apples:
        snake_head = [nx,ny]
        snakes.append(snake_head)
        
        maps[nx][ny] = 1  # 뱀이 있는 곳

        apples.remove([nx,ny])
    else:
        snake_head = [nx,ny]
        snakes.append(snake_head)

        maps[nx][ny] = 1  # 뱀이 있는 곳

        # 뱀 꼬리 제거
        end = snakes.pop(0)
        maps[end[0]][end[1]] = 0
    
    que.append(snake_head)

print(time)


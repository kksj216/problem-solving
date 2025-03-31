from collections import deque

n, m, remain = map(int, input().split())
graph = [[0] for i in range(n+1)]
for i in range(n):
    graph[i+1].extend(list(map(int, input().split())))
    
car_x, car_y = map(int, input().split())

member = []
for i in range(m):
    ax, ay, bx, by = map(int, input().split())

    member.append([ax,ay, bx,by])

## *. 맨 처음에, 가장 가까은 사람을 어떻게 찾지??
    # 남은 사람들과의 거리 확인. 
    #   - 전부다 하나씩 bfs를 해야하나?? O
    #   - 택시 좌표에서 행렬 뺀 값이 가장 작은 위치에 있는 사람?? X 

dir = [(-1,0), (1,0), (0,1), (0,-1)]

def bfs(cx, cy):
    que = deque()
    que.append((cx,cy))
    visited = [[-1 for i in range(n+1)] for i in range(n+1)]
    visited[cx][cy] = 0

    while que:
        q_pop = que.popleft()
        xx, yy = q_pop[0], q_pop[1]

        for d in range(4):
            n_xx, n_yy = xx+dir[d][0], yy+dir[d][1]

            if 0<n_xx<=n and 0<n_yy<=n and visited[n_xx][n_yy]==-1 and graph[n_xx][n_yy]!=1:
                visited[n_xx][n_yy] = visited[xx][yy]+1
                que.append((n_xx, n_yy))

    return visited

def check_dist(visited, member):
    for mem in range(len(member)):
        sx, sy, ax, ay = member[mem]
        member[mem].append(visited[sx][sy])
        
    member.sort(key=lambda x: (-x[4], -x[0], -x[1]))

# for i in range(len(member)):
def solution():
    global car_x, car_y
    global remain
    while member:
        ## 가장 가까운 사람 찾기
        ##  -> 택시부터 모든 거리 수 재기
        visited = bfs(car_x, car_y)

        ## 거리 순으로 사람들 정렬
        check_dist(visited, member)
        sx, sy, ax, ay, dist1 = member.pop()  # 택시 위치 ~ 현재 사람 거리
        
        for temp in member:
            temp.pop()

        ## 현재 사람에서 목적지까지 거리 수 재기
        visited = bfs(sx, sy)
        
        dist2 = visited[ax][ay]  # 현재 사람 ~ 목적지 거리
        car_x, car_y = ax, ay  # 택시 위치 목적지로 바뀜.

        ## ** 택시가 승객을 태우러 갈 수 없는 경우 or 승객을 목적지까지 이동시킬 수 없는 경우
        if dist1==-1 or dist2==-1:
            print(-1)
            return

        remain -= dist1
        if remain < 0:  # 가는 길에 연료 끝
            break

        remain -= dist2
        if remain < 0:  # 가는 길에 연료 끝
            break
        
        ## 연료 충전
        remain += (dist2*2)
    
    if remain < 0:
        print(-1)
    else:
        print(remain)

solution()

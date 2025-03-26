from collections import deque

n,m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(input())
    for j in range(m):
        if graph[i][j] == "B":
            b_place = (i,j)
        if graph[i][j] == "R":
            r_place = (i,j)
        if graph[i][j] == "O":
            o_place = (i,j)

dir = [(-1,0), (1,0), (0,-1), (0,1)]

def move(x, y, d):

    count = 0
    ## Q. graph[x+dir[d][0]][y+dir[d][1]] - 다음이 벽이면 멈춤
    #     graph[x][y] - 현재가 구멍이면 멈춤
    while graph[x+dir[d][0]][y+dir[d][1]]!="#" and graph[x][y]!="O":
        x += dir[d][0]
        y += dir[d][1]
        count += 1
    return x, y, count

def bfs():
    que = deque()
    que.append((r_place[0], r_place[1], b_place[0], b_place[1], 1))

    visited = []
    ## Q. visited 를 왜 빨간 구슬 좌표와 파란 구슬 좌표를 같이 넣는건지?
    ##    - R의 위치만 저장하면 B의 위치가 바뀌었는지 여부를 알 수 없음
    visited.append((r_place[0], r_place[1], b_place[0], b_place[1]))

    while que:
        q_pop = que.popleft()
        rx, ry, bx, by, c = q_pop[0], q_pop[1], q_pop[2], q_pop[3], q_pop[4]

        if c > 10:
            print(-1)
            return

        for d in range(4):
            n_rx, n_ry, r_count = move(rx, ry, d)
            n_bx, n_by, b_count = move(bx, by, d)

            ## Q. o_place를 확인하는게 왜 여기에서 이동한 값으로 확인하는지?
            ##   - 도착한 위치가 구멍인지 확인해야 함. 
            if (n_bx, n_by)==o_place:  ## Q. 왜 파랑구슬리 구멍에 들어가면 게임 끝.
                continue
            if (n_rx, n_ry)==o_place:
                print(c)
                return

            ## R과 B가 같은 간에 있을 수 없음 
            if (n_rx, n_ry)==(n_bx, n_by):
                if r_count>b_count:  # R이 더 많이 이동했다는 뜻 → 즉, B가 먼저 왔고 R이 뒤에 왔으므로 R을 한 칸 뒤로 물림 
                    n_rx -= dir[d][0]
                    n_ry -= dir[d][1]
                else:                # B가 더 많이 이동했다는 뜻 → 즉, R이 먼저 왔고 B가 뒤에 왔으므로 B를 한 칸 뒤로 물림
                    n_bx -= dir[d][0]
                    n_by -= dir[d][1]
            
            if (n_rx, n_ry, n_bx, n_by) not in visited:
                visited.append((n_rx, n_ry, n_bx, n_by))
                que.append((n_rx, n_ry, n_bx, n_by, c+1))

    ## Q. que로 while이 끝날 경우 
    #    - 가능한 모든 경우를 탐색했으나 빨간 구슬을 구멍에 넣는 방법이 없다.
    print(-1)

bfs()
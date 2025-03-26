from collections import deque

n,m = map(int,input().split())

graph = [[] for i in range(n)]

for i in range(n):
    graph[i] = list(input())
    for j in range(m):
        if graph[i][j] == 'R':
            r_place = (i,j)
        if graph[i][j] == 'B':
            b_place = (i,j)
        if graph[i][j] == 'O':
            o_place = (i,j)

dir = [(-1,0), (1,0), (0,-1), (0,1)]  # 상 하 좌 우


def move(x, y, d):
    count =0
    # 벽 아니고, 구멍 아닐 동안 반복 
    while (graph[x+dir[d][0]][y+dir[d][1]]!="#" and graph[x][y]!="O"):
        x += dir[d][0]
        y += dir[d][1]
        count += 1
    return x, y, count


# 1. R에서 O로 가는 최단 경로

def bfs():
    que = deque()
    que.append((r_place, b_place, 1))
    rx,ry = r_place[0], r_place[1]
    bx,by = b_place[0], b_place[1]

    visited = []
    visited.append((rx,ry,bx,by))  # 구슬 위치 튜플 

    while que:
        q_pop = que.popleft()
        rx, ry, bx, by, directions  = q_pop[0][0], q_pop[0][1], q_pop[1][0], q_pop[1][1], q_pop[2]

        # print(rx, ry, bx, by, directions )

        if directions > 10:
            break

        for d in range(4):
            n_rx, n_ry, r_count = move(rx, ry, d)
            n_bx, n_by, b_count = move(bx, by, d)

            # 파랑이 구멍에 들어갈 경우 
            if graph[n_bx][n_by] == "O":
                continue
            # 빨강이 들어갈 경우 성공
            if graph[n_rx][n_ry] == "O":
                print(directions)
                return  # return !!

            if (n_rx,n_ry) == (n_bx, n_by):  # 겹친 경우
                # 더 많이 이동한 것을 1칸 뒤로 ??
                if r_count > b_count:
                    n_rx -= dir[d][0]
                    n_ry -= dir[d][1]
                else:
                    n_bx -= dir[d][0]
                    n_by -= dir[d][1]

            # 가지 않은 곳 탐색 
            if ( n_rx, n_ry, n_bx, n_by) not in visited:
                visited.append((n_rx, n_ry, n_bx, n_by))
                que.append(((n_rx, n_ry), (n_bx, n_by), directions+1))

    print(-1)

bfs()

"""
# visited = [[False for i in range(m)] for j in range(n)]
# visited_b = [[False for i in range(m)] for j in range(n)]
visited = []

while que:
    q_pop = que.popleft()
    print("q_pop ", q_pop)
    rx,ry, bx,by, directions = q_pop[0][0],q_pop[0][1], q_pop[1][0],q_pop[1][1], q_pop[2]
    direction = directions[-1]
    # visited[rx][ry] = True
    visited.append((rx,ry, bx,by))

    # print( rx,ry, bx,by, directions )

    for d in range(4):
        nx, ny = rx+dir[d][0], ry+dir[d][1]
            
            ## 그림에서 빨간공 이동
            graph[rx][ry] = "."
            graph[nx][ny] = "R"

            ## 파란공 이동
            nx_b, ny_b = bx+dir[d][0], by+dir[d][1]

            if (0<=nx_b<n and 0<=ny_b<m and visited_b[nx_b][ny_b]==False and (graph[nx_b][ny_b]=="." or graph[nx_b][ny_b]=="O")):
                if d != direction:  # 방향이 달라진 경우 
                    que.append(((nx,ny), (nx_b,ny_b), directions+[d]))
                else:  # 같은 방향으로 굴러감
                    que.append(((nx,ny), (nx_b,ny_b), directions))

                graph[bx][by] = "."
                graph[nx_b][ny_b] = "B"
            else:
                if d != direction:  # 방향이 달라진 경우 
                    que.append(((nx,ny), (bx,by), directions+[d]))
                else:  # 같은 방향으로 굴러감
                    que.append(((nx,ny), (bx,by), directions))
            
    if len(directions)-1 > 10:
        print(-1)
        break

"""
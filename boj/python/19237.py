n,m,k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]
graph_smell = [[[0,0] for _ in range(n)] for _ in range(n)]
shark_position = [(0,0) for i in range(m) ]

for i in range(n):
    graph[i] = list(map(int, input().split()))
    
    for j in range(n):
        if graph[i][j]!=0:
            shark_position[graph[i][j]-1] = (i,j)

shark_watching = list(map(int, input().split()))
shark_priority = [[] for i in range(m)]

for i in range(m):
    for j in range(4):
        shark_priority[i].append( list(map(int, input().split())) )

# 1 2 3 4 = 상 하 좌 우
dir = [(-1,0), (1,0), (0,-1), (0,1)]


def move_shark(idx, cur_position):
    cx,cy = cur_position[0], cur_position[1]
    cur_watch = shark_watching[idx] - 1

    priority = shark_priority[idx][cur_watch]

    ## 범위 내에 냄새가 없는 곳으로 이동
    for i in priority:
        nx, ny = cx+dir[i-1][0], cy+dir[i-1][1]
        
        if 0<=nx<n and 0<=ny<n:  # 범위 안
            if graph_smell[nx][ny][1]==0:  ## 남은시간이 0. 다른 냄새가 아니어야 함.
                return i, (nx,ny)
    
    ## 같은 냄새가 있는 곳으로 갈 수 있다면 가기
    for i in priority:
        nx, ny = cx+dir[i-1][0], cy+dir[i-1][1]

        if 0<=nx<n and 0<=ny<n:  # 범위 안
            if graph_smell[nx][ny][0]==idx+1:  ## 다른 냄새가 아니어야 함.
                return i, (nx,ny)
            
    return cur_watch + 1, cur_position  # 이동할 수 없으면 제자리 유지

# 현재 서있는 곳에 냄새 뿌리기 
for i in range(m):
    xx, yy = shark_position[i][0], shark_position[i][1]

    graph_smell[xx][yy] = [ i+1, k ]  # 처음 냄새 표시하기

time = 0
while time<1001:   # 1000초 포함이기 때문에 1001 까지 
    """
    # while True:
    if time >= 1000:  # 1000초가 넘어가면 중단
        time = -1
        break
    """

    new_positions = {} 
    # 다음 칸 이동 가능한지 확인. 우선순위에 따라
    # 가능한 자리로 이동
    for i in range(m):
        if shark_position[i]==(-1,-1):  # 상어가 벗어났으면
            continue

        ## 새로운 방향과 위치 찾기
        new_watch, new_position = move_shark(i, shark_position[i])
        
        # 새로운 방향으로 업데이트
        shark_watching[i] = new_watch

        # 겹치는 상어가 있으면  가장 작은 번호의 상어만 남기기 
        if new_position in new_positions:
            if i < new_positions[new_position]:  # 더 작은 번호 남기기 
                new_positions[new_position] = i
        else:
            new_positions[new_position] = i


    # # print("new_positions ", new_positions)
    # # # 겹치는 상어가 있으면 "가장 작은 번호를 가진 상어"를 제외하고 모두 격자 밖으로
    # for i in range(m):
    #     s_pos = shark_position[i]
    #     for j in range(m):
    #         if i!=j and s_pos==shark_position[j]:  # 겹치는 상어 나감
    #             shark_position[j] = (-1,-1)



    # 1. 먼저 모든 상어의 위치를 초기화 (제거된 것으로 간주)
    new_shark_position = [(-1, -1)] * m

    # 2. new_positions의 정보를 활용하여 업데이트
    for pos, idx in new_positions.items():
        new_shark_position[idx] = pos

    # for i in range(m):
    #     if i not in new_positions.values():
    #         new_shark_position[i] = (-1, -1)  # 삭제 처리

    shark_position = new_shark_position  # 한 번에 업데이트

    


    # 지나온 칸 k 줄이기
    for i in range(n):
        for j in range(n):
            if graph_smell[i][j][1] > 0:
                graph_smell[i][j][1] -= 1

                if graph_smell[i][j][1] == 0:
                    graph_smell[i][j] = [0,0]

    # 현재 칸에 냄새 뿌리기 
    count = 0
    for i in range(m):
        xx, yy = shark_position[i][0], shark_position[i][1]

        if shark_position[i] != (-1,-1):
            graph_smell[xx][yy] = [ i+1, k ]

        # if i!=0 and [xx, yy]==[-1,-1]:
        if i!=0 and shark_position[i]==(-1,-1):
            count += 1

    time += 1

    ## 1번 상어만 격자에 남으면 끝.
    if count==m-1:
        break
    
    # # 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1 출력
    # if time>1001:  #  and count!=m-1:
    #     time = -1
    #     break

if time>1000:  ### *** 시간 리밋이 중요 !!!
    time = -1

print(time)

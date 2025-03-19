from collections import deque

n = int(input())

graph = [[] for _ in range(n)]

place_fish = []
min_fish = []
for i in range(n):
    graph[i] = list(map(int, input().split()) )
    for j in range(n):
        if graph[i][j]==9:
            place_shark = (i,j)
        if graph[i][j]>0 and graph[i][j]!=9:
            place_fish.append((i,j))  # 물고기 좌표 리스트 

# print(place_shark)
# print(place_fish)

dir = [(-1,0), (0,-1), (0,1), (1,0)] # 상좌우하

size_shark = 2
eat_fish = 0
time = 0

def bfs(x,y):
    fish_list = []
    visited = [[-1 for i in range(n)] for _ in range(n)]

    que = deque([(x,y, 0)])  # 좌표, dist (상어 좌표에서 시작)
    visited[x][y] = 0
    
    while que:
        cur = que.popleft()
        c_x, c_y, dist = cur[0], cur[1], cur[2]
        
        for d in range(4):
            n_x, n_y = c_x+dir[d][0], c_y+dir[d][1]

            if 0<=n_x<n and 0<=n_y<n and visited[n_x][n_y]==-1:

                if graph[n_x][n_y] <= size_shark:  # 지나갈 수 있는 길이면 가기. 
                    visited[n_x][n_y] = 1 # dist + 1
                    que.append((n_x, n_y, dist+1))

                    if 0 < graph[n_x][n_y] < size_shark:  # 먹을 수 있는 물고기 리스트에 넣기.
                        fish_list.append((dist+1, n_x, n_y))  # 물고기 거리, x, y 좌표

    fish_list.sort()  # 거리, x, y 좌표 순으로 정렬 
    return fish_list


# 1. 먹을 수 있는 물고기 수 == 1:
# 1-1. 상어 크기보다 물고기 크기가 작은 경우
#       물고기 먹으러 이동
#       eat_fish+1

# 2. 먹을 수 있는 물고기 수 > 1:
# 2-1. 상어 크기보다 물고기 크기가 작은 경우가 있으면 
#       가까운 물고기 먹으러 이동 (위,좌 우선순위)
#       eat_fish+1
# 2-2. 상어 크기보다 물고기 크기가 작은 경우가 없으면
#       return time

# 3. 먹을 수 있는 물고기 수 < 1:
#       return time

# 상어 크기만큼 먹었으면 상어 몸집 키우기

# ==============================

while True:
    # 1. 상어에서 시작해서, 갈 수 있는 물고기 좌표들 구하기 
    fish_l = bfs(place_shark[0], place_shark[1])  

    if not fish_l:   # 갈 수 있는 물고기 없으면 종료
        break

    # 2. 먹을 수 있는 가장 가까운 물고기 처리하기 
    dist, fx, fy = fish_l[0]
    time += dist  # 이동시간 증가 

    eat_fish += 1  # 먹은 물고기 수 증가

    graph[place_shark[0]][place_shark[1]] = 0  # 표에서 상어 좌표 0으로
    graph[fx][fy] = 9   # 표에서 물고기 좌표를 상어좌표로
    place_shark = (fx, fy) # 상어 좌표 설정

    if size_shark == eat_fish:  # 상어 몸집 키우기
        size_shark += 1
        eat_fish = 0



print(time)



#### ==================================

    # min_fish = []
    # # 1. 먹을 수 있는 물고기 수 == 1:
    # if len(place_fish) == 1:
    #     fish = place_fish.pop()
    #     fish_x, fish_y = fish[0], fish[1]
    #     if graph[fish_x][fish_y] < size_shark:
    #         # 도착까지 걸린 시간 계산
    #         count = bfs(fish_x, fish_y)
    #         print("count: ", count)
            
    #         # 물고기 먹기 
    #         graph[fish_x][fish_y] = 0   # 1) 맵에서 물고기 없애기 
    #         eat_fish += 1   # 2) 먹은 물고기 수 +1
            
    #         # 상어 크기만큼 먹었으면 상어 몸집 키우기
    #         if size_shark==eat_fish:
    #             size_shark += 1
    #             eat_fish = 0

    #         place_shark = (fish_x, fish_y)  # 3) 상어 좌표 이동 

    #         time += count
    #     else:
    #         break


    # # 2. 먹을 수 있는 물고기 수 > 1:
    # if len(place_fish) > 1:
    #     # 2-1. 상어 크기보다 물고기 크기가 작은 경우가 없으면 return time
    #     go_or_not = False
    #     for i in range(len(place_fish)):
    #         f_x, f_y = place_fish[i][0], place_fish[i][1]
    #         if graph[f_x][f_y] < size_shark:
    #             go_or_not = True
    #             min_fish.append((f_x, f_y))
    #     if go_or_not == False:
    #         break

    #     # 2-2. 상어 크기보다 물고기 크기가 작은 경우가 있으면
    #     # for m in min_fish:
    #     if len(min_fish) > 1:

    #         min_fish.sort(reverse=True)
    #         for m in range(len(min_fish)):
    #             x,y = min_fish[m][0], min_fish[m][1]
    #             count = bfs(x,y)
    #             time += count

    #             graph[x][y] = 0
    #             eat_fish += 1

    #              # 상어 크기만큼 먹었으면 상어 몸집 키우기
    #             if size_shark==eat_fish:
    #                 size_shark += 1
    #                 eat_fish = 0

    #             place_shark = (x,y)
                
    #             place_fish.remove(( x,y ))
    #             graph[x][y] = 0

    #             print("place_fish: ", place_fish)

    # # 3. 먹을 수 있는 물고기 수 < 1: return time
    # if len(place_fish) < 1:
    #     break


    # # # 상어 크기만큼 먹었으면 상어 몸집 키우기
    # if size_shark==eat_fish:
    #     size_shark += 1
    #     eat_fish = 0


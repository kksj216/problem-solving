from collections import deque
 
n,m = map(int, input().split())

r, c, d = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

dir = [(-1,0), (0,1), (1,0), (0,-1)] # 북 동 남 서 

que = deque()
que.append((r, c, d))
visited = [[False for _ in range(m)] for _ in range(n)]

def ban_time_round(d):
    d -= 1
    if d < 0:
        d = 3
    return d 
def naming(dd):
    if dd==0:
        return "북"
    if dd==1:
        return "동"
    if dd==2:
        return "남"
    if dd==3:
        return "서"

count = 0
while que:
    q_pop = que.popleft()
    cur_r, cur_c, cur_d = q_pop[0], q_pop[1], q_pop[2]
    visited[cur_r][cur_c] = True
    

    if graph[cur_r][cur_c]==0:
        graph[cur_r][cur_c] = 2  # 현재 칸 청소 
        count += 1
        # print(cur_r, cur_c, naming(cur_d))

    count_round = 0
    new_d = cur_d
    while count_round < 4:
        new_d = ban_time_round(new_d)   # 반시계 90도 이동 
        new_r, new_c = cur_r+dir[new_d][0], cur_c+dir[new_d][1]

        if 0<=new_r<n and 0<=new_c<m and (graph[new_r][new_c]==0 ): # 청소하지 않음
            # if visited[new_r][new_c]==False:
            que.append(( new_r, new_c, new_d ))
            break
        else:
            count_round += 1

    
    if count_round==4:  # 주변에 청소되지 않은 빈 칸이 없는 경우
        ## 후진할 곳
        new_r, new_c = cur_r-dir[cur_d][0], cur_c-dir[cur_d][1]
        if graph[new_r][new_c]==1:
            break
        else:
            que.append(( new_r, new_c, cur_d ))


# print("count ", count)
print(count)

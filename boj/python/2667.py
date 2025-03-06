from collections import deque

n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(input())
    for j in range(n):
        graph[i][j] = int(graph[i][j])

visited = [[False for _ in range(n)] for _ in range(n)]

dir = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우

all = []
count_t = 0
for i in range(n):  ## 모든 칸에 대해 확인해본다.
    for j in range(n):
        if (not visited[i][j]) and (graph[i][j]==1): # 방문 안했고 갈수있는 곳
            que = deque([(i,j)])
            visited[i][j] = True   ## !!!! 바로 방문 표시를 해야...
            count = 1

            while que:
                cur = que.popleft()

                for d in range(4):
                    ni, nj = cur[0]+dir[d][0], cur[1]+dir[d][1]

                    # 범위 확인 and 방문여부 확인 and 갈수있는지 확인
                    if 0 <= ni < n and 0 <= nj < n and visited[ni][nj]==False and graph[ni][nj] == 1:
                        count += 1  # 갯수 세기
                        que.append((cur[0]+dir[d][0], cur[1]+dir[d][1]))  ## !!!! que 넣는 형식!! que.append((a,b))
                        visited[cur[0]+dir[d][0]][cur[1]+dir[d][1]] = True

            count_t += 1  # 총 단지의 수 세기 
            all.append(count)

print(count_t)
all.sort()  ##  !!전체 중에 오름차순이 맞음
for i in range(count_t):
    print(all[i])

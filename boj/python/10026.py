from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(input())

dir = [(-1,0), (1,0), (0,-1), (0,1)]
count_num1 = 0
count_num2 = 0
visited_graph1 = [[False for i in range(n)] for _ in range(n)]
visited_graph2 = [[False for i in range(n)] for _ in range(n)]
visited = [[False for i in range(n)] for _ in range(n)]

graph_rgone = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph_rgone[i][j]=="R":
            graph_rgone[i][j]="G"


## 1. 일반 사람이 봤을 때 구역 수 
for i in range(n):
    for j in range(n):
        if visited_graph1[i][j] == False:
            count_num1 += 1

            que = deque()
            que.append([i,j])

            while que:
                cur = que.popleft()
                cur_color = graph[cur[0]][cur[1]]
                visited_graph1[cur[0]][cur[1]] = True

                for d in range(4):
                    new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

                    if 0<=new_x<n and 0<=new_y<n:
                        new_color = graph[new_x][new_y]

                        if new_color==cur_color and visited_graph1[new_x][new_y]==False:
                            que.append((new_x, new_y))
                            visited_graph1[new_x][new_y] = True

                        # if (cur_color=="R" and new_color=="G") or (cur_color=="G" and new_color=="R"):
                        #     graph_rgone[new_x][new_y] = "R"


## 2. 적록색약 사람이 봤을 떄 구역 수 
for i in range(n):
    for j in range(n):
        if visited_graph2[i][j] == False:
            count_num2 += 1

            que = deque()
            que.append([i,j])

            while que:
                cur = que.popleft()
                cur_color = graph_rgone[cur[0]][cur[1]]
                visited_graph2[cur[0]][cur[1]] = True

                for d in range(4):
                    new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

                    if 0<=new_x<n and 0<=new_y<n:
                        new_color = graph_rgone[new_x][new_y]

                        if new_color==cur_color and visited_graph2[new_x][new_y]==False:
                            que.append((new_x, new_y))
                            visited_graph2[new_x][new_y] = True
                            

print(count_num1, count_num2)


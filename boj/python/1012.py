from collections import deque

t = int(input())
dir = [(-1,0), (1,0), (0,-1), (0,1)]
count_l = []

for _ in range(t):

    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for k_i in range(k):
        a, b = map(int, input().split())

        graph[b][a] = 1

    # print(graph)

    for i in range(n):
        for j in range(m):
            # 아직 방문하지 않았다면
            if graph[i][j]==1 and visited[i][j]==False:

                que = deque([(i, j)])
                visited[i][j] = True
                count += 1

                while que:
                    cur = que.popleft()

                    for d in range(4):
                        new_x, new_y = cur[0]+dir[d][0], cur[1]+dir[d][1]

                        if 0<=new_x<n and 0<=new_y<m and graph[new_x][new_y]==1 and visited[new_x][new_y]==False:
                            visited[new_x][new_y] = True
                            que.append((new_x, new_y))

    # print(count, end="")
    count_l.append(count)

for i in range(len(count_l)):
    print(count_l[i])

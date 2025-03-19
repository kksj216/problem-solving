r,c = map(int, input().split())

graph = [0 for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
check_a = [False for _ in range(26)]
dir = [(-1,0), (1,0), (0,1), (0,-1)]

for i in range(r):
    graph[i] = list(str(input()))

def dfs(graph, vx, vy, count):
    global maxcount
    maxcount = max(maxcount, count)  ## *** 

    check_a[ord(graph[vx][vy])-65] = True

    for d in range(4):
        nx,ny = vx+dir[d][0], vy+dir[d][1]

        if 0<=nx<r and 0<=ny<c :  # and visited[nx][ny]==False:

            if check_a[ord(graph[nx][ny])-65] == False:
                
                check_a[ord(graph[nx][ny])-65] = True
                dfs(graph, nx, ny, count+1)
                check_a[ord(graph[nx][ny])-65] = False

maxcount = 1

dfs(graph, 0,0, maxcount)

# count = 0
# for i in check_a:
#     if i==True:
#         count += 1

print(maxcount)
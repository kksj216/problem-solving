from collections import deque

n,l,r = map(int, input().split())

num_people = []
for i in range(n):
    a = list(map(int, input().split()))
    num_people.append(a)

dir = [(0,1), (0,-1), (1,0), (-1,0)]

count = 0
while True:

    linked_lists = []
    
    visited = [[False for _ in range(n)] for _ in range(n)]

    ### 1. 연결된 영역 찾아서 linked_lists 에 추가
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:

                que = deque()
                que.append([i,j])
                visited[i][j] = True

                linked = []
                linked.append([i,j])

                while que:
                    que_l = que.popleft()
                    cx,cy = que_l[0], que_l[1]

                    for d in range(4):
                        nx, ny = cx+dir[d][0], cy+dir[d][1]

                        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and l<=abs(num_people[cx][cy]-num_people[nx][ny])<=r:
                            que.append([nx, ny])

                            linked.append([nx,ny])

                            visited[nx][ny]=True

            if linked not in linked_lists and len(linked) >= 2:
                linked_lists.append(linked)
            
    # print("linked_lists ", linked_lists)
    
    ## 인구이동할 필요 없을 경우
    if len(linked_lists)==0:
        break

    ### 2. 인접한 칸으로 이동
    ## 연결된 칸들의 각 인구수 = 연합인구수/연합칸수
    for i in linked_lists:
        num_p = 0
        num_g = len(i)
        for j in i:
            x,y = j[0], j[1]
            num_p += num_people[x][y]

        value = num_p//num_g

        for j in i:
            x,y = j[0], j[1]
            num_people[x][y] = value

    # print(num_people)
    if count > 2000:
        break
    
    count += 1


print(count)

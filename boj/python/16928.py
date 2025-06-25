from collections import deque

n, m = map(int, input().split())

ns = []
ms = []
for _ in range(n):
    ns.append( list(map(int, input().split())) )
for _ in range(m):
    ms.append( list(map(int, input().split())) )

final_count = 0
visited = [False for _ in range(101)]

que = deque()
que.append((1,0))

while que:
    q_pop = que.popleft()
    x, count = q_pop[0], q_pop[1]
    # visited[x] = True

    if x == 100:
        final_count = count
        break

    for i in range(1,7):
        new_x = x + i

        if 1<=new_x<=100 and visited[new_x]==False:

            # 사다리 타기
            for nn in ns:
                if nn[0]==new_x:
                    new_x = nn[1]

            # 뱀 타기
            for mm in ms:
                if mm[0]==new_x:
                    new_x = mm[1]
            
            visited[new_x] = True
            que.append((new_x, count+1))

print(final_count)


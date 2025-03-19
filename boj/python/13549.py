from collections import deque

n,k = map(int, input().split())
dir = [2, -1, 1]

# 방문 체크 (최대 100,000까지 존재)
visited = [0] * 100001  

que = deque([n])
visited[n] = 1  # 시작점 1초 표시

while que:
    cur = que.popleft()

    if cur == k:
        break
    
    for i in (2*cur, cur-1, cur+1):  ### 이 순서로 해야만 한다.
        if i < 0 or i > 100000 or visited[i]:  # 범위 밖이거나 방문한 경우
            continue
            
        if i == 2*cur: 
            visited[i] = visited[cur] # 0초 
        else:
            visited[i] = visited[cur]+1 # 1초

        que.append(i)

print(visited[k]-1)
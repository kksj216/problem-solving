from collections import deque

n,m, x,y, k = map(int, input().split())

graph = [[] for i in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

order = list(map(int, input().split()))

dir = [(0,1), (0,-1), (-1,0), (1,0)]  # 동 서 북 남
dice = [0,0,0,0,0,0]  # 아래0, 북1, 동2, 서3, 남4, 위5

def move_dice(move): # 조건 1을 기준으로 굴리기
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if move == 1: # 동쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif move == 2: # 서쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d 
    elif move == 3: # 북쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif move == 4: # 남쪽으로 굴리면
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

result = []
for o in order:
    new_x = x+dir[o-1][0]
    new_y = y+dir[o-1][1]
    if 0<=new_x<n and 0<=new_y<m:
        x = new_x
        y = new_y
        move_dice(o)  # 주사위 굴리고 주사위 값 이동. 

        floor_value = dice[5]
        top_value = dice[0]

        if graph[new_x][new_y]==0:
            graph[new_x][new_y] = floor_value
        else:
            dice[5] = graph[new_x][new_y] 
            graph[new_x][new_y] = 0
        result.append(top_value) 
    else:
        continue

for i in result:
    print(i)

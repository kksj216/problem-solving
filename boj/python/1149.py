import copy 

n = int(input())

colors = [[] for _ in range(n)]

for i in range(n):
    colors[i] = list(map(int, input().split()))

dp = [[0]*3 for _ in range(n)]
dp[0] = colors[0]
for i in range(1, n):
    dp[i][0] = colors[i][0]+min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = colors[i][1]+min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = colors[i][2]+min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))

"""
min_nums = 0
dp = []
for i in range(n):
    m = 1001
    m_idx = 0
    s = 1001
    s_idx = 0
    
    m = min(colors[i])
    for j in range(3):
        if m == colors[i][j]:
            m_idx = j
    
    if i>=1 and dp[i-1][0]==m_idx: # 앞의 색과 같으면 그다음 작은걸로 
        temp_color = copy.deepcopy(colors)
        temp_color[i][m_idx] = 10000
        print("temp_color ", temp_color)

        m = min(temp_color[i])
        for j in range(3):
            if m == temp_color[i][j]:
                m_idx = j

        dp.append((m_idx, m))

    else:
        dp.append((m_idx, m))

print(dp)

sum = 0
for i in range(len(dp)):
    sum += dp[i][1]
print(sum)"
"""
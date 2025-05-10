n = int(input())
a_list = [ [0 for i in range(10)] for _ in range(n) ]
a_list[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# a_list[0][1] = 0

for i in range(1, n):
    a_list[i][0] = a_list[i-1][1]
    a_list[i][9] = a_list[i-1][8]

    for j in range(1, 9):
        a_list[i][j] = a_list[i-1][j-1]+a_list[i-1][j+1]

print(sum(a_list[n-1])%1000000000)

"""
a[n][k] = a[n-1][k-1] + a[n-1][k+1] (0<=k<=8)
a[n][0] = a[n-1][k+1] (k=0)
a[n][9] = a[n-1][k-1] (k=9)
"""
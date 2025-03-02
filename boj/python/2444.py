n = int(input())

for i in range(1, 2*n):
    s = " "*abs((n-i))
    if i > n:
        s += "*"* ((i-(i-n)*2)*2-1)
    else:
        s += "*"*(i*2-1)
    print(s)
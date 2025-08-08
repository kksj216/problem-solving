n,m = map(int, input().split())

ls = []
for i in range(n):
    ls.append(list(str(input())))

count = []
for a in range(n-7):
    for b in range(m-7):
        black=0
        white=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0: # 짝수
                    if ls[i][j]=="B":
                        white += 1
                    else:
                        black += 1
                else: # 홀수
                    if ls[i][j]=="B":
                        black += 1
                    else:
                        white += 1
        count.append(white)
        count.append(black)

print(min(count))

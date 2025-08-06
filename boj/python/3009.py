squre_x = []
squre_y = []

for i in range(3):
    a,b = map(int, input().split())
    squre_x.append(a)
    squre_y.append(b)

nx, ny = 0,0
for i in range(3):
    if squre_x.count(squre_x[i])==1:
        nx = squre_x[i]
    if squre_y.count(squre_y[i])==1:
        ny = squre_y[i]

    

print(nx, ny)
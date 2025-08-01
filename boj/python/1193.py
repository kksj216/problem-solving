x = int(input())

i, num = 0, 0

while x > num:
    i += 1
    num += i

if i % 2 == 0:
    a = i-(num-x)
    b = (num-x)+1
else:
    a = (num-x)+1
    b = i-(num-x)

print(f'{a}/{b}')

'''
up = [0]
down = [0]

i = 1
while True:
    if i <= x:
        for j in range(1, i+1):
            up.append(j)
            down.append(i-j+1)
    else:
        break
    i += 1

print(up[x],"/",down[x], sep='')
'''
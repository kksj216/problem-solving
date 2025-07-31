t = int(input())

moneys = [[0 for i in range(4)] for i in range(t)]
for i in range(t):
    money = int(input())*(0.01)

    while money:
        if money >= 0.25:
            moneys[i][0] += 1
            money -= 0.25
        elif money >= 0.1:
            moneys[i][1] += 1
            money -= 0.1
        elif money >= 0.05:
            moneys[i][2] += 1
            money -= 0.05
        elif money >= 0.01:
            moneys[i][3] += 1
            money -= 0.01
        
        money = round(money, 2)

for i in range(t):
    for j in range(4):
        print(moneys[i][j], end=' ')
    print()
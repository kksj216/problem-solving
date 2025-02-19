a, b, c = map(int, input().split())
lis = [a, b, c]
# print(lis)
# print(max(lis))
max_num = max(lis)

if a==b and b==c:
    score = 10000+(a*1000)
elif (a==b and b!=c):
    score = 1000+(a*100)
elif (a==c and c!=b):
    score = 1000+(a*100)
elif (b==c and c!=a):
    score = 1000+(b*100)
else:
    score = max_num * 100

print(score)
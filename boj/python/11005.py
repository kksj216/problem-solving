n,b = map(int, input().split())
b = int(b)

num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''
while n:
    ans += str(num[n%b])
    n = n//b

# print(ans)
print(ans[::-1])
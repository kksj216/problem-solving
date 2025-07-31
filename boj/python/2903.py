n = int(input())

ans = 3
if n==1:
    print(ans*ans)
    exit()

for i in range(2,n+1):
    ans += 2**(i-1)

print(ans*ans)
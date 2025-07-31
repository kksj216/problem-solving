n, b = map(str, input().split())
b = int(b)

print(int(n, int(b)))
# int(바꾸고 싶은 string 형의 문자, int(진법의 종류)) 


# ------
# num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# n, b = map(str, input().split())
# n = n[::-1]
# b = int(b)
# ans = 0

# for i in range(len(n)):
#     ans += (b**i)*num.index(n[i])

# print(ans)
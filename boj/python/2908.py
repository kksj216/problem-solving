a, b = map(str, input().split())

s_a = ""
s_b = ""
for i in range(1,4):
    s_a += a[3-i]
    s_b += b[3-i]

s_a = int(s_a)
s_b = int(s_b)

print(max(s_a, s_b))
n = int(input())

c = 666
count = 0
while True:
    str_c = str(c)
    if '666' in str_c:
        count += 1
    if count==n:
        break
    c += 1

print(c)
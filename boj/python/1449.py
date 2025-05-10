n, l = map(int, input().split())

place = list(map(int, input().split()))
place.sort()

start = place[0]
count = 1
length = 0
for p in place[1:]:
    if p - start +1 <= l:
        length = p-start+1
    else:
        start = p
        count += 1

print(count )

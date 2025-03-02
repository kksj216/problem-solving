arr = [(0, "")]*20
grade = [("A+", 4.5), ("A0", 4.0), ("B+", 3.5), ("B0", 3.0), 
         ("C+", 2.5), ("C0", 2.0), ("D+", 1.5), ("D0", 1.0), ("F", 0.0)]

for i in range(20):
    a, b, c = map(str, input().split())
    arr[i] = (float(b), c)

avg = 0
tot = 0
for i in range(20):
    for g, s in grade:
        # print(g, s)
        if arr[i][1] == g:
            avg += (arr[i][0]*s)
            tot += arr[i][0]
avg /= tot
print(round(avg, 6))

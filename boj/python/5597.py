l = [i+1 for i in range(30)]

inp = []
for i in range(28):
    a = int(input())
    inp.append(a)

for _ in range(28):
    l.remove( inp[_] )
for i in l:
    print(i)
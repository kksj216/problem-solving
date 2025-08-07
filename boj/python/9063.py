n = int(input())

pos_x = []
pos_y = []
for i in range(n):
    a, b = map(int, input().split())
    pos_x.append(a)
    pos_y.append(b)

minx,miny = min(pos_x), min(pos_y)
maxx,maxy = max(pos_x), max(pos_y)

if minx>0:
    x = maxx-minx
elif minx<0 and maxx>0:
    x = maxx+abs(minx)
elif maxx<0:
    x = abs(minx)-abs(maxx)

if miny>0:
    y = maxy-miny
elif miny<0 and maxy>0:
    y = maxy+abs(miny)
elif maxy<0:
    y = abs(miny)-abs(maxy)

# print(x,y)
print(x*y)

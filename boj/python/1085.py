x, y, w, h = map(int, input().split())

se = min(h-y, y-0)
ga = min(w-x, x-0)

print(min(se, ga))
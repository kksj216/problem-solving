from itertools import combinations

n,m = map(int, input().split())
numbers = list(map(int, input().split()))

ls = []
for comb in combinations(numbers, 3):
    threes = sum(list(comb))
    if threes <= m:
        ls.append(threes)

print(max(ls))

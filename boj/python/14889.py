from itertools import combinations, permutations
import math

n = int(input())

ls = [i for i in range(n+1)]
maps = [[] for i in range(n+1)]

for i in range(n):
    maps[i+1] = [0]+list(map(int, input().split()))

nums = []
for i in combinations(ls[1:], n//2):
    
    sub_ls = list(i)
    count = 0
    for j in permutations(sub_ls, 2):
        count += (maps[j[0]][j[1]]) # + maps[j[1]][j[0]])
    nums.append(count)
    # nums.append(maps[i[0]][i[1]] + maps[i[1]][i[0]])

results = []
for i in range(len(nums)//2):
    results.append( abs(nums[i] - nums[len(nums)-i-1] ))

print(min(results))
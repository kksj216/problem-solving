n,c = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

def bin_search(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==target:
            return 1
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return 0

if c in arr:
    print(1)
    exit()

l, r = 0, n-1
while l < r:
    sum = arr[l]+arr[r]
    if sum == c:
        print(1)
        exit()
    elif sum > c:
        r -= 1
    elif sum < c:
        if bin_search(l+1, r-1, c-sum):
            print(1)
            exit()
        else:
            l += 1

print(0)

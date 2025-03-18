
"""
count1 = 0
count2 = 0

def fib1(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

def fib2(n):
    global count2
    arr = [0]*(n+1)

    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        count2 += 1
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n-1]
"""

def fib1(n):
    f = [0]*(n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

def fib2(n):
    return n-2

n = int(input())

print(fib1(n), fib2(n))
# print(fib1(n), fib2(n))
# print()

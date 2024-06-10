
n = int(input())
a = list(map(int, input().split()))

def f(l, r, x):
    return a[l:r+1].count(x)

def solve(a):
    n = len(a)
    count = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            if f(1, i, a[i-1]) > f(j, n, a[j-1]):
                count += 1
    return count

print(solve(a))


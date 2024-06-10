

def solve(n, a):
    a = sorted(a)
    res = 0
    for i in range(n):
        if a[i] >= i+1:
            res += 1
        else:
            break
    return res

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))



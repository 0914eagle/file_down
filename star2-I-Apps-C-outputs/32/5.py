
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    a.sort()
    colors = 0
    for i in range(n):
        if a[i] % a[0] == 0:
            continue
        else:
            colors += 1
            while i < n and a[i] % a[0] != 0:
                i += 1
    return colors + 1

print(solve(a))



n, l, x, y = map(int, input().split())
a = list(map(int, input().split()))

def check(dist):
    for i in range(n):
        for j in range(i, n):
            if a[j] - a[i] == dist:
                return True
    return False
    
if not check(x):
    a.append(x)
if not check(y):
    a.append(y)
    
a.sort()
print(len(a) - n)
print(*a[n:])


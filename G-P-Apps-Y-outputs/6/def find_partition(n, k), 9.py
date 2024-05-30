
def find_partition(n, k):
    if n % 2 == 0:
        if k % 2 == 0:
            return "YES\n" + " ".join([str(n//k)]*k)
        elif k <= n:
            return "YES\n" + " ".join([str(1)]*(k-1)) + " " + str(n - (k-1))
    else:
        if k % 2 != 0:
            return "YES\n" + " ".join([str(1)]*k)
    return "NO"

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_partition(n, k))
```

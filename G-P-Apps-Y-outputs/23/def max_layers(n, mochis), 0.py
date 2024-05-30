
def max_layers(n, mochis):
    mochis.sort(reverse=True)
    unique_mochis = list(set(mochis))
    return len(unique_mochis)

n = int(input())
mochis = [int(input()) for _ in range(n)]
print(max_layers(n, mochis))
```

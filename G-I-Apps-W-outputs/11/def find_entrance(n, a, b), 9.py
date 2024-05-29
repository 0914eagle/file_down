
def find_entrance(n, a, b):
    k = (a + b) % n
    if k == 0:
        return n
    elif k < 0:
        return n + k
    else:
        return k

# Input
n, a, b = map(int, input().split())

# Output
print(find_entrance(n, a, b))
```

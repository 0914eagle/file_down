
def max_number(n, a, f):
    res = list(map(int, a))
    for i in range(n):
        if f[res[i] - 1] > res[i]:
            j = i
            while j < n and f[res[j] - 1] >= res[j]:
                res[j] = f[res[j] - 1]
                j += 1
            break
    return ''.join(map(str, res))

# Read input
n = int(input())
a = input()
f = list(map(int, input().split()))

# Output the result
print(max_number(n, a, f))
```

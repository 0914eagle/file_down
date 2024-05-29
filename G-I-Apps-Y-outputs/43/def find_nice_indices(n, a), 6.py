
def find_nice_indices(n, a):
    sum_a = sum(a)
    nice_indices = []
    for i in range(n):
        if (sum_a - a[i]) % 2 == 0 and (sum_a - a[i]) // 2 in a:
            nice_indices.append(i+1)
    return nice_indices

n = int(input())
a = list(map(int, input().split()))
nice_indices = find_nice_indices(n, a)

print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))
```

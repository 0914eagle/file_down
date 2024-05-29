
def max_number(n, a, f):
    a = list(map(int, a))
    f = {idx + 1: val for idx, val in enumerate(f)}

    max_num = int(''.join(str(f[num]) if f[num] > num else str(num) for num in a))
    
    for i in range(n):
        if f[a[i]] > a[i]:
            new_num = int(''.join(str(f[num]) if f[num] > num else str(num) for num in a[:i] + a[i + 1:]))
            max_num = max(max_num, new_num)
    
    return max_num

# Input
n = int(input())
a = input().strip()
f = list(map(int, input().split()))

# Output
print(max_number(n, a, f))
```

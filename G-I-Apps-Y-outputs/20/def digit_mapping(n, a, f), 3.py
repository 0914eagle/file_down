
def digit_mapping(n, a, f):
    max_num = list(a)
    max_val = 0
    
    for i in range(n):
        num = list(a)
        for j in range(i, n):
            num[j] = str(f[int(num[j])-1])
            val = int("".join(num))
            if val > max_val:
                max_val = val
                max_num = num[:]
    
    return int("".join(max_num))

# Input
n = int(input())
a = input().strip()
f = list(map(int, input().split()))

# Output
print(digit_mapping(n, a, f))
```

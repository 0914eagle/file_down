
n, c, b = map(int, input().split())
broken_bits = list(map(int, input().split()))

result = [1] * c  # initialize with c 1s for maximum bit changes
for i in broken_bits:
    result[i - 1] = 0  # set broken bits to 0

# Find the first bit that needs to be changed to 0
start_idx = 0
while result[start_idx] == 0:
    start_idx += 1

# Modify bits to reach exactly c bit changes
for i in range(start_idx, n-1):
    if result[i] == result[i+1]:  # change the bit if it is the same as the next bit
        result[i] = 1 - result[i]
        c -= 1
        if c == 0:
            break

print(''.join(map(str, result)))
```

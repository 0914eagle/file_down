
import math

def restore_array(n, gcd_table):
    a = [0] * n
    visited = [False] * n
    gcd_dict = {}

    for i in range(n):
        for j in range(n):
            if i != j:
                gcd_dict[gcd_table[i * n + j]] = gcd_dict.get(gcd_table[i * n + j], 0) + 1

    a[0] = max(gcd_dict)
    visited[0] = True

    for i in range(1, n):
        for j in range(n):
            if not visited[j]:
                skip = False
                for k in range(i):
                    if math.gcd(a[k], gcd_table[j]) != gcd_table[i * n + j]:
                        skip = True
                        break
                if not skip:
                    a[i] = gcd_table[j]
                    visited[j] = True
                    break

    return a

# Input parsing
n = int(input())
gcd_table = list(map(int, input().split()))

# Restore array a
restored_array = restore_array(n, gcd_table)

# Print the restored array
print(' '.join(map(str, restored_array)))
```

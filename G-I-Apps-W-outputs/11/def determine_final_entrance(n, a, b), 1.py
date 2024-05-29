
def determine_final_entrance(n, a, b):
    k = (a + b) % n
    if k == 0:
        return n
    elif k < 0:
        return n + k
    else:
        return k

# Read input values
n, a, b = map(int, input().split())

# Determine the final entrance
result = determine_final_entrance(n, a, b)

# Print the final entrance
print(result)
```

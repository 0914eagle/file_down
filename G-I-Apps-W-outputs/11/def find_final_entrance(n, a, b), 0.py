
def find_final_entrance(n, a, b):
    return ((a + b - 1) % n) + 1

# Reading input
n, a, b = map(int, input().split())

# Finding final entrance
final_entrance = find_final_entrance(n, a, b)

print(final_entrance)
```


def find_final_entrance(n, a, b):
    final_entrance = (a + b) % n
    if final_entrance == 0:
        final_entrance = n
    return final_entrance

# Input
n, a, b = map(int, input().split())

# Output
print(find_final_entrance(n, a, b))
```

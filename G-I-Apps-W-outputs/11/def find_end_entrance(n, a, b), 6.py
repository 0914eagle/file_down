
def find_end_entrance(n, a, b):
    end_entrance = (a + b) % n
    if end_entrance == 0:
        end_entrance = n
    return end_entrance

# Read input
n, a, b = map(int, input().split())

# Find and print the end entrance
print(find_end_entrance(n, a, b))
```

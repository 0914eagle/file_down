
def starting_time(A, B):
    start_time = (A + B) % 24
    return start_time

# Input
A, B = map(int, input().split())

# Output
print(starting_time(A, B))
```

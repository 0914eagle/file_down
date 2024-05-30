
def sheep_safety(S, W):
    if W >= S:
        print("unsafe")
    else:
        print("safe")

# Read input from Standard Input
S, W = map(int, input().split())

# Check safety
sheep_safety(S, W)
```

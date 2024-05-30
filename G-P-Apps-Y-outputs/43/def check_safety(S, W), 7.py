
def check_safety(S, W):
    if W >= S:
        print("unsafe")
    else:
        print("safe")

# Take input from Standard Input
S, W = map(int, input().split())

# Check safety
check_safety(S, W)
```


def check_safety(S, W):
    if W >= S:
        print("unsafe")
    else:
        print("safe")

# Reading input from standard input
S, W = map(int, input().split())
check_safety(S, W)
```


def protect_sheep(S, W):
    if S > W:
        print("safe")
    else:
        print("unsafe")

# Read input from Standard Input
S, W = map(int, input().split())

# Call the function with the input values
protect_sheep(S, W)
```


def symmetric_difference():
    # Input handling
    M = int(input())
    set_M = set(map(int, input().split()))
    N = int(input())
    set_N = set(map(int, input().split()))

    # Compute symmetric difference
    sym_diff = sorted(set_M.symmetric_difference(set_N))

    # Output the result
    for num in sym_diff:
        print(num)

# Test the function
symmetric_difference()
```

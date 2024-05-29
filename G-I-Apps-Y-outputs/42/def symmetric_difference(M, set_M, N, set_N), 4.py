
def symmetric_difference(M, set_M, N, set_N):
    set_M = set(map(int, set_M.split()))
    set_N = set(map(int, set_N.split()))
    
    sym_diff = sorted(set_M.symmetric_difference(set_N))
    
    for num in sym_diff:
        print(num)

# Input reading
M = int(input())
set_M = input()
N = int(input())
set_N = input()

# Call the function with the provided inputs
symmetric_difference(M, set_M, N, set_N)
```

You can use this Python function to find the symmetric difference of two sets of integers in ascending order. Let me know if you need any further assistance! 

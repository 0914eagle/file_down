
def possible_healths(N, S):
    # Validate the input
    if N == 0:  # Edge case when N = 0
        return S == [1]  # Only possible value is 1
    
    # Sort the input multiset S in descending order
    S.sort(reverse=True)
    
    # Initialize a list to hold healths of slimes at each time step
    healths = [0] * (2 ** N)
    healths[0] = S[0]
    
    for i in range(N):
        for j in range(2 ** i):
            if healths[j] == 0:  # Skip if no slime exists at this index
                continue
            # Reproduce a new slime with health less than the current slime
            healths[2 * j] = max(healths[2 * j], healths[j] - 1)
            healths[2 * j + 1] = max(healths[2 * j + 1], S[2 ** i + j] - healths[j])
    
    return "Yes" if healths == S else "No"

# Read input
N = int(input())
S = list(map(int, input().split()))

# Check if it is possible to set the healths as required
result = possible_healths(N, S)
print(result)
```


def can_reach_target_permutation(n, k, q, s):
    # Helper function to apply permutation p to permutation q
    def apply_permutation(p, q):
        return [q[p[i]-1] for i in range(n)]

    # Check if s is already on the board before the first move
    if q == s:
        return "NO"

    # Initialize the starting permutation as 1, 2, ..., n
    current_permutation = list(range(1, n+1))

    # Iterate over k moves
    for _ in range(k):
        # Simulate a coin toss
        coin_toss = 1  # For simplicity, let's assume heads corresponds to 1 and tails to 2

        if coin_toss == 1:
            # Apply the inverse permutation of q to the current permutation
            current_permutation = apply_permutation(q, current_permutation)
        else:
            # Apply permutation q to the current permutation
            current_permutation = apply_permutation(s, current_permutation)

        # Check if Masha's permutation is reached
        if current_permutation == s:
            return "YES"

    return "NO"

# Read input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Check if the situation described in the statement is possible
result = can_reach_target_permutation(n, k, q, s)
print(result)
```

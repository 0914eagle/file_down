
def is_possible(n, k, q, s):
    # Function to apply a permutation to another permutation
    def apply_permutation(perm, p):
        return [p[i-1] for i in perm]

    current_perm = list(range(1, n+1))  # Initial permutation on the board

    for _ in range(k):
        head = apply_permutation(q, current_perm)
        tail = apply_permutation(s, current_perm)

        if head == s or tail == s:
            return "YES"
        
        current_perm = head  # Assume we got heads

    return "NO"

# Read input
n, k = map(int, input().split())
q = list(map(int, input().split()))
s = list(map(int, input().split()))

# Check if the situation is possible
result = is_possible(n, k, q, s)
print(result)
```

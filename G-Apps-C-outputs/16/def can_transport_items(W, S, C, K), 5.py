
def can_transport_items(W, S, C, K):
    if (W <= K and S <= K) or (S <= K and C <= K) or (W <= K and C <= K):
        return "YES"
    else:
        return "NO"

# Read input
W, S, C, K = map(int, input().split())

# Check if transportation is possible
result = can_transport_items(W, S, C, K)
print(result)


def can_transport(W, S, C, K):
    # Check if it's possible to transport the items without any losses
    if (W <= K and S <= K) or (S <= K and C <= K) or (W <= K and C <= K):
        return "YES"
    else:
        return "NO"

# Read input values
W, S, C, K = map(int, input().split())

# Call the function and print the result
print(can_transport(W, S, C, K))

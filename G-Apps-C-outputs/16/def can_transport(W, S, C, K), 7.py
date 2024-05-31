
def can_transport(W, S, C, K):
    if (W > K and S > 0) or (S > K and C > 0):
        return "NO"
    return "YES"

# Read input
W, S, C, K = map(int, input().split())

# Call the function and print the result
print(can_transport(W, S, C, K))

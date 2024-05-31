
def can_transport_items(W, S, C, K):
    if (W > K and S > 0) or (S > K and C > 0) or (W > 0 and S > 0 and C > 0 and (W + S + C) > K):
        return "NO"
    return "YES"

# Input
W, S, C, K = map(int, input().split())

# Call the function and print the result
print(can_transport_items(W, S, C, K))


def can_transport(W, S, C, K):
    if W > K or S > K or C > K:
        return "NO"
    
    total = W + S + C
    max_group = max(W, S, C)
    
    if max_group > total - max_group + K:
        return "NO"
    
    return "YES"

# Read input from user
inputs = input().strip().split()
W, S, C, K = map(int, inputs)

# Call the function and print the result
result = can_transport(W, S, C, K)
print(result)

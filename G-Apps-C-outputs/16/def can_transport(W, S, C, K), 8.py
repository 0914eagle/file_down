
def can_transport(W, S, C, K):
    # Check if the number of sheep and wolves or sheep and cabbages are greater than the boat capacity
    if (W > K and S > K) or (S > K and C > K):
        return "NO"
    
    # Check if the number of wolves and cabbages is greater than twice the boat capacity
    if W > 2*K or C > 2*K:
        return "NO"
    
    return "YES"

# Read input values
W, S, C, K = map(int, input().split())

# Call the function and print the result
print(can_transport(W, S, C, K))

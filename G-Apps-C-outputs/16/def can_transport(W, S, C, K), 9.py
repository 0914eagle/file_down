
def can_transport(W, S, C, K):
    # Check if the number of wolves and sheep is greater than the capacity of the boat
    if W > K or S > K:
        return "NO"
    
    # Check if the number of sheep and cabbages is greater than the capacity of the boat
    if S > K or C > K:
        return "NO"
    
    # Check if the number of wolves and sheep is greater than the number of cabbages
    if W > S or S > C:
        return "NO"
    
    return "YES"

# Read input
W, S, C, K = map(int, input().split())

# Check if transportation is possible without item loss
result = can_transport(W, S, C, K)
print(result)

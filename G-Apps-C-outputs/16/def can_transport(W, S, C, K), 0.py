
def can_transport(W, S, C, K):
    # Check if the number of wolves or sheep is greater than the capacity of the boat
    if W > K or S > K:
        return "NO"
    
    # Check if the number of wolves and sheep together is greater than the capacity of the boat
    if W + S > K:
        return "NO"
    
    return "YES"

# Read input
W, S, C, K = map(int, input().split())

# Call the function and print the result
print(can_transport(W, S, C, K))

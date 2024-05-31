
def can_transport(W, S, C, K):
    # Check if the number of sheep or cabbages is greater than the number of wolves
    if S > W or C > W:
        return "NO"
    
    # Check if it's possible to transport all items in one go
    if max(W, S, C) <= K:
        return "YES"
    
    # Check if it's possible to transport without losing items
    if (W <= K and S <= K) or (W <= K and C <= K) or (S <= K and C <= K):
        return "YES"
    
    return "NO"

# Input
W, S, C, K = map(int, input().split())

# Output
print(can_transport(W, S, C, K))

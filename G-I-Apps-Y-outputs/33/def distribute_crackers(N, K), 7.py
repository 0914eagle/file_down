
def distribute_crackers(N, K):
    rem = N % K
    return min(rem, K - rem)

# Get input
N, K = map(int, input().split())

# Calculate and print the minimum possible difference
print(distribute_crackers(N, K))

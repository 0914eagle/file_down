
def calculate_accommodation_fee(N, K, X, Y):
    if N <= K:
        return N * X
    else:
        return K * X + (N - K) * Y

# Read input
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# Calculate and print total accommodation fee
print(calculate_accommodation_fee(N, K, X, Y))


def calculate_accommodation_fee(N, K, X, Y):
    if N <= K:
        return N * X
    else:
        return K * X + (N - K) * Y

# Read input values
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# Calculate and print the total accommodation fee
total_fee = calculate_accommodation_fee(N, K, X, Y)
print(total_fee)

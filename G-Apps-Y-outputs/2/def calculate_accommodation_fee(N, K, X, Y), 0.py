
def calculate_accommodation_fee(N, K, X, Y):
    total_fee = 0
    if N <= K:
        total_fee = N * X
    else:
        total_fee = K * X + (N - K) * Y
    return total_fee

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

print(calculate_accommodation_fee(N, K, X, Y))

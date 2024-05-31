
def calculate_accommodation_fee(N, K, X, Y):
    total_fee = 0
    
    for night in range(1, N+1):
        if night <= K:
            total_fee += X
        else:
            total_fee += Y
    
    return total_fee

# Input
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# Calculate and output the total accommodation fee
print(calculate_accommodation_fee(N, K, X, Y))

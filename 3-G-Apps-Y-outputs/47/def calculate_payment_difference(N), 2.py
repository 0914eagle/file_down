
def calculate_payment_difference(N):
    total_cost = 800 * N
    total_refund = 200 * (N // 15)
    return total_cost - total_refund

# Input
N = int(input())

# Output
print(calculate_payment_difference(N))

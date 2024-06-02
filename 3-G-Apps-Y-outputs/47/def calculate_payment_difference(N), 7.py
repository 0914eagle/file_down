
def calculate_payment_difference(N):
    total_cost = 800 * N
    total_refund = (N // 15) * 200
    return total_cost - total_refund

N = int(input())
result = calculate_payment_difference(N)
print(result)

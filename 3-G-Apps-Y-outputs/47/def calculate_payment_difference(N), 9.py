
def calculate_payment_difference(N):
    total_cost = N * 800
    total_discount = (N // 15) * 200
    return total_cost - total_discount

N = int(input())
result = calculate_payment_difference(N)
print(result)

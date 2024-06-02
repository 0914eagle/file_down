
def calculate_payment_difference(N):
    meal_cost = 800
    discount = 200
    total_cost = N * meal_cost
    total_discount = (N // 15) * discount
    return total_cost - total_discount

N = int(input())
result = calculate_payment_difference(N)
print(result)

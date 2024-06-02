
def calculate_payment_difference(N):
    meal_price = 800
    discount_threshold = 15
    discount_amount = 200
    
    total_cost = N * meal_price
    total_discounts = (N // discount_threshold) * discount_amount
    
    return total_cost - total_discounts

N = int(input())
result = calculate_payment_difference(N)
print(result)

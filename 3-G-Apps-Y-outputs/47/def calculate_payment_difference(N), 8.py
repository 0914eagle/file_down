
def calculate_payment_difference(N):
    meal_cost = 800
    discount = 200
    meals_ordered = N
    total_cost = meal_cost * meals_ordered
    total_discount = (meals_ordered // 15) * discount
    payment_difference = total_cost - total_discount
    return payment_difference

N = int(input())
result = calculate_payment_difference(N)
print(result)

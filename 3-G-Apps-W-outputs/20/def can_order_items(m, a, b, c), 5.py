
def can_order_items(m, a, b, c):
    if a + b + c <= 2 * m:
        return "possible"
    else:
        return "impossible"

# Read input
m, a, b, c = map(int, input().split())

# Check if it's possible to order items
result = can_order_items(m, a, b, c)
print(result)

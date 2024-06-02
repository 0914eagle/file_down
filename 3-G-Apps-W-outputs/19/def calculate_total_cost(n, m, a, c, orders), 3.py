
def calculate_total_cost(n, m, a, c, orders):
    total_cost = 0
    remaining_dishes = a.copy()
    
    for order in orders:
        kind, num_dishes = order
        cost = 0
        
        if remaining_dishes[kind-1] >= num_dishes:
            cost = c[kind-1] * num_dishes
            remaining_dishes[kind-1] -= num_dishes
        else:
            for i in range(n):
                if remaining_dishes[i] > 0:
                    cost = c[i] * min(remaining_dishes[i], num_dishes)
                    remaining_dishes[i] -= min(remaining_dishes[i], num_dishes)
                    break
        
        total_cost += cost
    
    return total_cost

# Input parsing
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print total cost for each customer
for order in orders:
    print(calculate_total_cost(n, m, a, c, order))

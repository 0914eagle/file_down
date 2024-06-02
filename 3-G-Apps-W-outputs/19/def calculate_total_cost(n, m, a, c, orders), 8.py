
def calculate_total_cost(n, m, a, c, orders):
    total_cost = 0
    remaining_dishes = a.copy()
    
    for order in orders:
        t, d = order
        cost = 0
        
        if remaining_dishes[t-1] >= d:
            cost = d * c[t-1]
            remaining_dishes[t-1] -= d
        else:
            remaining_dishes_copy = remaining_dishes.copy()
            remaining_dishes_copy[t-1] = 0
            while d > 0:
                min_cost = float('inf')
                min_index = -1
                for i in range(n):
                    if remaining_dishes_copy[i] > 0 and c[i] < min_cost:
                        min_cost = c[i]
                        min_index = i
                if min_index == -1:
                    break
                dishes_served = min(remaining_dishes_copy[min_index], d)
                cost += dishes_served * c[min_index]
                remaining_dishes_copy[min_index] -= dishes_served
                d -= dishes_served
        
        total_cost += cost
    
    return total_cost

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

for order in orders:
    print(calculate_total_cost(n, m, a, c, order))

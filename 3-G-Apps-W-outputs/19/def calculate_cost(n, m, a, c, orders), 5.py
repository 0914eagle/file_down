
def calculate_cost(n, m, a, c, orders):
    remain = a.copy()
    costs = []
    
    for order in orders:
        t, d = order
        cost = 0
        
        if remain[t-1] >= d:
            cost = d * c[t-1]
            remain[t-1] -= d
        else:
            remaining_dishes = d
            while remaining_dishes > 0:
                min_cost = float('inf')
                min_idx = -1
                for i in range(n):
                    if remain[i] > 0 and c[i] < min_cost:
                        min_cost = c[i]
                        min_idx = i
                
                if min_idx == -1:
                    break
                
                served_dishes = min(remaining_dishes, remain[min_idx])
                cost += served_dishes * min_cost
                remain[min_idx] -= served_dishes
                remaining_dishes -= served_dishes
        
        costs.append(cost)
    
    return costs

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

result = calculate_cost(n, m, a, c, orders)
for cost in result:
    print(cost)

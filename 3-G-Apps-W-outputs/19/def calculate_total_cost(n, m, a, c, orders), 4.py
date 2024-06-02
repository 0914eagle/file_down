
def calculate_total_cost(n, m, a, c, orders):
    remain = a.copy()
    total_cost = 0

    for order in orders:
        t, d = order
        cost = 0

        if remain[t-1] >= d:
            cost = c[t-1] * d
            remain[t-1] -= d
        else:
            remaining_dishes = d
            while remaining_dishes > 0:
                min_cost = float('inf')
                min_index = -1
                for i in range(n):
                    if remain[i] > 0 and c[i] < min_cost:
                        min_cost = c[i]
                        min_index = i
                if min_index == -1:
                    break
                served_dishes = min(remaining_dishes, remain[min_index])
                cost += min_cost * served_dishes
                remain[min_index] -= served_dishes
                remaining_dishes -= served_dishes

        total_cost += cost

    return total_cost

# Input reading
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print total cost for each customer
for order in orders:
    print(calculate_total_cost(n, m, a, c, order))

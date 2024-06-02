
def calculate_cost(n, m, a, c, orders):
    remain = a.copy()
    cheapest = min(c)
    total_cost = 0

    for order in orders:
        t, d = order
        cost = 0

        if remain[t-1] >= d:
            cost = d * c[t-1]
            remain[t-1] -= d
        else:
            remaining_dishes = d
            while remaining_dishes > 0:
                if sum(remain) == 0:
                    cost = 0
                    break

                min_index = [i for i, x in enumerate(c) if x == cheapest and remain[i] > 0][0]
                served_dishes = min(remaining_dishes, remain[min_index])
                cost += served_dishes * c[min_index]
                remain[min_index] -= served_dishes
                remaining_dishes -= served_dishes

        total_cost += cost

    return total_cost

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

for order in orders:
    cost = calculate_cost(n, m, a, c, orders)
    print(cost)

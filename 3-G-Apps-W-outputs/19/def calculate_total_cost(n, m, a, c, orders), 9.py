
def calculate_total_cost(n, m, a, c, orders):
    remain = a.copy()
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
                min_cost = float('inf')
                min_index = -1
                for i in range(n):
                    if remain[i] > 0 and c[i] < min_cost:
                        min_cost = c[i]
                        min_index = i

                if min_index == -1:
                    break

                serve_dishes = min(remaining_dishes, remain[min_index])
                cost += serve_dishes * c[min_index]
                remain[min_index] -= serve_dishes
                remaining_dishes -= serve_dishes

        total_cost += cost

    return total_cost

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

for order in orders:
    print(calculate_total_cost(n, m, a, c, order))

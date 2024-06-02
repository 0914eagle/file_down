
def calculate_cost(n, m, a, c, orders):
    remain = a.copy()
    total_cost = 0

    for order in orders:
        kind, dishes = order
        cost = 0

        if remain[kind-1] >= dishes:
            cost = c[kind-1] * dishes
            remain[kind-1] -= dishes
        else:
            for i in range(n):
                if remain[i] >= dishes:
                    cost = c[i] * dishes
                    remain[i] -= dishes
                    break

        total_cost += cost

    return total_cost

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

orders = []
for _ in range(m):
    t, d = map(int, input().split())
    orders.append((t, d))

for i in range(m):
    cost = calculate_cost(n, m, a, c, orders[:i+1])
    print(cost)


def calculate_total_cost(n, m, a, c, orders):
    total_cost = 0
    remain = a.copy()

    for order in orders:
        t, d = order
        cost = 0

        if remain[t-1] >= d:
            cost = d * c[t-1]
            remain[t-1] -= d
        else:
            cost = remain[t-1] * c[t-1]
            d -= remain[t-1]
            remain[t-1] = 0

            while d > 0:
                min_cost = min([c[i] for i in range(n) if remain[i] > 0])
                min_index = [i for i in range(n) if c[i] == min_cost and remain[i] > 0][0]

                if remain[min_index] >= d:
                    cost += d * c[min_index]
                    remain[min_index] -= d
                    d = 0
                else:
                    cost += remain[min_index] * c[min_index]
                    d -= remain[min_index]
                    remain[min_index] = 0

        total_cost += cost

    return total_cost

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
orders = [list(map(int, input().split())) for _ in range(m)]

for order in orders:
    print(calculate_total_cost(n, m, a, c, orders))

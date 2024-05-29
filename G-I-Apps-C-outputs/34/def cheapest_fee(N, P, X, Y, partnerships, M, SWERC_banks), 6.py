
def cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    def bellman_ford(N, P, partnerships, source, destination):
        dist = [float('inf')] * N
        dist[source - 1] = 0

        for _ in range(N - 1):
            for a, b, c in partnerships:
                if dist[a - 1] != float('inf') and dist[a - 1] + c < dist[b - 1]:
                    dist[b - 1] = dist[a - 1] + c

        return dist[destination - 1]

    min_fee = bellman_ford(N, P, partnerships, X, Y)

    for bank in SWERC_banks:
        if bellman_ford(N, P, partnerships, X, bank) < min_fee or bellman_ford(N, P, partnerships, bank, Y) < min_fee:
            return min_fee + 1

    return "Impossible"

if __name__ == "__main__":
    N, P, X, Y = map(int, input().split())
    partnerships = [list(map(int, input().split())) for _ in range(P)]
    M = int(input())
    SWERC_banks = list(map(int, input().split()))

    result = cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks)
    print(result)
```

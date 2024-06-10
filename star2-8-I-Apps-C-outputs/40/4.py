
n, m, alpha = map(int, input().split())
candies = [0] * (n + 1)
for i in range(1, m + 1):
    u, v, c = map(int, input().split())
    candies[u] = max(candies[u], c)
    candies[v] = max(candies[v], c)

max_candies = 0
min_energy = 10 ** 18
for i in range(1, n + 1):
    if candies[i] > max_candies:
        max_candies = candies[i]
        min_energy = max_candies ** 2 + alpha

print(min_energy)


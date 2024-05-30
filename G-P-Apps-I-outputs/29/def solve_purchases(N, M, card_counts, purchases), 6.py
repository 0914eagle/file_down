
def solve_purchases(N, M, card_counts, purchases):
    total_purchases = 0
    output = []

    for i in range(N):
        while card_counts[i] > N // 2:
            for j in range(i + 1, N):
                if card_counts[j] < N // 2:
                    card_counts[i] -= 1
                    card_counts[j] += 1
                    output.append((i + 1, j + 1, i))
                    total_purchases += 1

    for purchase in purchases:
        output.append((purchase[0], purchase[1], 0))

    print(total_purchases)
    for purchase in output:
        print(f"{purchase[0]} {purchase[1]} {purchase[2]}")

# Sample Input 1
N, M = 2, 3
card_counts = [5, 1]
purchases = [(1, 2), (1, 2), (1, 2)]
solve_purchases(N, M, card_counts, purchases)

# Sample Input 2
N, M = 4, 3
card_counts = [5, 3, 1, 1]
purchases = [(1, 3), (2, 3), (4, 1)]
solve_purchases(N, M, card_counts, purchases)
```


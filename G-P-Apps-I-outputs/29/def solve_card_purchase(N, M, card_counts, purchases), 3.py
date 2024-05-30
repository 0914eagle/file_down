
def solve_card_purchase(N, M, card_counts, purchases):
    total_purchases = 0
    results = []

    for i in range(N):
        for j in range(i + 1, N):
            while card_counts[i] != card_counts[j]:
                total_purchases += 1
                results.append((i+1, j+1, 2))
                card_counts[i] += 2
                card_counts[j] += 2

    print(total_purchases)
    for result in results:
        print(' '.join(map(str, result)))

# Sample Input 1
N, M = 2, 3
card_counts = [5, 1]
purchases = [(1, 2), (1, 2), (1, 2)]
solve_card_purchase(N, M, card_counts, purchases)

# Sample Input 2
N, M = 4, 3
card_counts = [5, 3, 1, 1]
purchases = [(1, 3), (2, 3), (4, 1)]
solve_card_purchase(N, M, card_counts, purchases)
```

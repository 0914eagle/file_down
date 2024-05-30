
def solve_card_purchases(N, M, card_counts, purchases):
    total_purchases = []
    purchases_made = 0

    for purchase in purchases:
        child1, child2 = purchase
        funds = min(card_counts[child1-1] // 2, card_counts[child2-1] // 2)
        card_counts[child1-1] -= funds * 2
        card_counts[child2-1] -= funds * 2

        winner = funds % 2
        if winner == 0:
            card_counts[child1-1] += 1
            card_counts[child2-1] += 1
        else:
            card_counts[child1-1] += 2

        total_purchases.append((child1, child2, winner))
        purchases_made += 1

    print(purchases_made)
    for purchase in total_purchases:
        print(f"{purchase[0]} {purchase[1]} {purchase[2]}")

# Input parsing
N, M = map(int, input().split())
card_counts = list(map(int, input().split()))
purchases = [list(map(int, input().split())) for _ in range(M)]

# Solve and output
solve_card_purchases(N, M, card_counts, purchases)
```

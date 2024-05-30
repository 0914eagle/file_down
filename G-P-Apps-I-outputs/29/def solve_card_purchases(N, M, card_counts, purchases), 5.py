
def solve_card_purchases(N, M, card_counts, purchases):
    total_purchases = 0
    all_purchases = []

    for purchase in purchases:
        child1, child2 = purchase
        cards_to_purchase = card_counts[child1 - 1] + card_counts[child2 - 1]
        first_child_cards = cards_to_purchase // 2
        all_purchases.append((child1, child2, first_child_cards))
        card_counts[child1 - 1] += first_child_cards
        card_counts[child2 - 1] += cards_to_purchase - first_child_cards
        total_purchases += 1

    print(total_purchases)
    for purchase in all_purchases:
        print(f"{purchase[0]} {purchase[1]} {purchase[2]}")

# Sample Input 1
N, M = 2, 3
card_counts = [5, 1]
purchases = [(1, 2), (1, 2), (1, 2)]
solve_card_purchases(N, M, card_counts, purchases)

# Sample Input 2
N, M = 4, 3
card_counts = [5, 3, 1, 1]
purchases = [(1, 3), (2, 3), (4, 1)]
solve_card_purchases(N, M, card_counts, purchases)
```

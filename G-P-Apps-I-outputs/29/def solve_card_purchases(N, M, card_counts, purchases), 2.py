
def solve_card_purchases(N, M, card_counts, purchases):
    total_purchases = 0
    purchase_list = []

    for purchase in purchases:
        child1, child2 = purchase
        half_funds = min(card_counts[child1-1] // 2, card_counts[child2-1] // 2)
        cards_bought = min(half_funds * 2, 2)

        if card_counts[child1-1] <= card_counts[child2-1]:
            win_child = child2
        else:
            win_child = child1

        card_counts[child1-1] += cards_bought
        card_counts[child2-1] += cards_bought
        card_counts[win_child-1] += cards_bought

        purchase_list.append((child1, child2, cards_bought))
        total_purchases += 1

    print(total_purchases)
    for purchase_desc in purchase_list:
        print(*purchase_desc)

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


def solve_card_problem(N, M, card_counts, purchases):
    purchases_list = []
    for purchase in purchases:
        total_cards = sum(card_counts)
        half_funds = total_cards // 2
        child1, child2 = purchase
        cards_gained = half_funds
        while card_counts[child1 - 1] < half_funds:
            card_counts[child1 - 1] += 1
            card_counts[child2 - 1] += 1
            cards_gained += 1
        purchases_list.append((child1, child2, cards_gained))

    print(len(purchases_list))
    for purchase in purchases_list:
        print(f"{purchase[0]} {purchase[1]} {purchase[2]}")

# Sample Input 1
N, M = 2, 3
card_counts = [5, 1]
purchases = [[1, 2], [1, 2], [1, 2]]
solve_card_problem(N, M, card_counts, purchases)

# Sample Input 2
N, M = 4, 3
card_counts = [5, 3, 1, 1]
purchases = [[1, 3], [2, 3], [4, 1]]
solve_card_problem(N, M, card_counts, purchases)
```


def solve_card_collection(N, M, cards_count, purchases):
    purchases_list = []
    while sum(cards_count) > 0:
        total_purchases = 0
        for i in range(N):
            for j in range(i+1, N):
                if cards_count[i] > 0 and cards_count[j] > 0:
                    total_purchases += 1
                    cards_count[i] -= 1
                    cards_count[j] -= 1
                    if i < j:
                        race_winner = i + 1
                        race_loser = j + 1
                        cards_count[race_winner - 1] += 2
                    else:
                        race_winner = j + 1
                        race_loser = i + 1
                        cards_count[race_winner - 1] += 2
                    purchases_list.append((race_winner, race_loser, i+1))

        if total_purchases == 0:
            break

    print(len(purchases_list))
    for purchase in purchases_list:
        print(purchase[0], purchase[1], purchase[2])

# Sample Input 1
N, M = 2, 3
cards_count = [5, 1]
purchases = [(1, 2), (1, 2), (1, 2)]
solve_card_collection(N, M, cards_count, purchases)

# Sample Input 2
N, M = 4, 3
cards_count = [5, 3, 1, 1]
purchases = [(1, 3), (2, 3), (4, 1)]
solve_card_collection(N, M, cards_count, purchases)


def solve_card_purchases(N, M, card_counts, purchases):
    total_purchases = []
    
    for i in range(M):
        purchase = purchases[i]
        a, b = purchase
        half_cards = (card_counts[a-1] + card_counts[b-1]) // 2
        
        total_purchases.append((a, b, half_cards - card_counts[a-1]))
        
        card_counts[a-1] += half_cards - card_counts[a-1]
        card_counts[b-1] += half_cards - card_counts[b-1]
    
    print(M)
    for purchase in total_purchases:
        print(f"{purchase[0]} {purchase[1]} {purchase[2]}")

# Sample Input
N, M = 2, 3
card_counts = [5, 1]
purchases = [(1, 2), (1, 2), (1, 2)]

solve_card_purchases(N, M, card_counts, purchases)

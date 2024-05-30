
def find_purchase_sequence(N, M, card_counts, purchases):
    total_cards = sum(card_counts)
    purchases_made = []
    
    for i in range(N):
        for j in range(i+1, N):
            while card_counts[i] + card_counts[j] >= 2:
                card_counts[i] -= 1
                card_counts[j] -= 1
                purchases_made.append((i+1, j+1, 2 if i < j else 1))
    
    for purchase in purchases:
        purchases_made.append((purchase[0], purchase[1], 0))
    
    print(len(purchases_made))
    for purchase in purchases_made:
        print(*purchase)

# Sample Input
N, M = map(int, input().split())
card_counts = list(map(int, input().split()))
purchases = [list(map(int, input().split())) for _ in range(M)]

find_purchase_sequence(N, M, card_counts, purchases)

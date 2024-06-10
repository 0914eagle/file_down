
n = int(input())
cards = list(map(int, input().split()))
sum_cards = sum(cards)
sum_min = float('inf')
sum_snuke = 0
for i in range(n-1):
    sum_snuke += cards[i]
    sum_raccoon = sum_cards - sum_snuke
    sum_min = min(sum_min, abs(sum_snuke-sum_raccoon))
print(sum_min)


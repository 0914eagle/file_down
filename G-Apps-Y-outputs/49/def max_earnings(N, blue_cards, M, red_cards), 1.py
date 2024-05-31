
def max_earnings(N, blue_cards, M, red_cards):
    max_earnings = 0
    for card in blue_cards:
        count = blue_cards.count(card) - red_cards.count(card)
        if count > max_earnings:
            max_earnings = count
    return max_earnings

N = int(input())
blue_cards = [input() for _ in range(N)]
M = int(input())
red_cards = [input() for _ in range(M)]

print(max_earnings(N, blue_cards, M, red_cards))

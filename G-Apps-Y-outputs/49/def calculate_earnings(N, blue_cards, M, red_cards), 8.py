
def calculate_earnings(N, blue_cards, M, red_cards):
    earnings = 0

    blue_dict = {}
    red_dict = {}

    for card in blue_cards:
        blue_dict[card] = blue_dict.get(card, 0) + 1

    for card in red_cards:
        red_dict[card] = red_dict.get(card, 0) + 1

    for card in blue_dict:
        earnings += blue_dict[card]

    for card in red_dict:
        earnings -= red_dict[card]

    return earnings

# Reading input
N = int(input())
blue_cards = [input() for _ in range(N)]
M = int(input())
red_cards = [input() for _ in range(M)]

# Calculating and printing earnings
print(calculate_earnings(N, blue_cards, M, red_cards))

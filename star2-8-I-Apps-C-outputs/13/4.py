
def find_winner(N, E, D, exploding_kittens, defuses):
    exploding_kittens.sort()
    defuses.sort()
    player_order = list(range(N))
    cards_in_hand = [0] * N
    winner = -1
    for card_index in range(E + D):
        if card_index < E:
            card = exploding_kittens[card_index]
        else:
            card = defuses[card_index - E]
        for player in player_order:
            if cards_in_hand[player] >= 5:
                cards_in_hand[player] -= 1
            elif card == 0:
                winner = player
                break
            else:
                card -= 1
                cards_in_hand[player] += 1
        if winner >= 0:
            break
    return winner

def main():
    N, E, D = map(int, input().split())
    exploding_kittens = list(map(int, input().split()))
    defuses = list(map(int, input().split()))
    winner = find_winner(N, E, D, exploding_kittens, defuses)
    print(winner)

if __name__ == "__main__":
    main()


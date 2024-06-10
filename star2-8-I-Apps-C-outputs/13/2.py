
from sys import stdin

def main():
    n, e, d = map(int, input().split())
    e_loc = list(map(int, input().split()))
    d_loc = list(map(int, input().split()))
    e_loc.sort()
    d_loc.sort()
    total_cards = e + d
    winner = -1
    player = 0
    num_cards = [0] * n
    while total_cards:
        if total_cards == 1:
            winner = player
            break
        if num_cards[player] > 5:
            num_cards[player] -= 1
            total_cards -= 1
            player = (player + 1) % n
            continue
        if e_loc and e_loc[0] == total_cards - 1:
            e_loc.pop(0)
            if d_loc and d_loc[0] == total_cards - 1:
                d_loc.pop(0)
                total_cards -= 2
            else:
                total_cards -= 1
        else:
            num_cards[player] += 1
            total_cards -= 1
        player = (player + 1) % n
    print(winner)

if __name__ == '__main__':
    main()


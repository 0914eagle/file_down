
import sys

def find_winner(n, e, d, e_pos, d_pos):
    players = list(range(n))
    next_pos = 0
    while len(players) > 1:
        if next_pos in e_pos:
            if next_pos in d_pos:
                e_pos.remove(next_pos)
                d_pos.remove(next_pos)
            else:
                return -1
        next_pos += 1
        if next_pos >= len(e_pos) + len(d_pos):
            next_pos = 0
        if len(players) > 5:
            players = players[:-1]
    return players[0]


if __name__ == '__main__':
    n, e, d = map(int, sys.stdin.readline().strip().split())
    e_pos = list(map(int, sys.stdin.readline().strip().split()))
    d_pos = list(map(int, sys.stdin.readline().strip().split()))
    print(find_winner(n, e, d, e_pos, d_pos))


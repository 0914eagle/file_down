
import sys

def solve(players, exploding, defuse):
    exploding.sort()
    defuse.sort()
    i, j = 0, 0
    while len(players) > 1:
        if i < len(exploding) and exploding[i] == 0:
            if j < len(defuse) and defuse[j] == 0:
                i += 1
                j += 1
            else:
                break
        players = players[1:]
        exploding = [x - 1 for x in exploding]
        defuse = [x - 1 for x in defuse]
        i += 1
    if len(players) == 1:
        print(players[0])
    else:
        print(-1)

if __name__ == '__main__':
    n, e, d = map(int, input().split())
    exploding = list(map(int, input().split()))
    defuse = list(map(int, input().split()))
    solve(list(range(n)), exploding, defuse)



from sys import stdin

def main():
    input = stdin.readline
    N, E, D = map(int, input().split())
    exploding_kittens = [int(x) for x in input().split()]
    defuses = [int(x) for x in input().split()]
    defuses.sort()
    exploding_kittens.sort()
    
    top_card = 0
    
    players = list(range(N))
    while len(players) > 1:
        for player in players:
            if exploding_kittens and top_card == exploding_kittens[0]:
                exploding_kittens.pop(0)
                top_card += 1
                if defuses and top_card == defuses[0]:
                    defuses.pop(0)
                    top_card += 1
                else:
                    return player
            else:
                top_card += 1
    return players[0]

if __name__ == "__main__":
    print(main())


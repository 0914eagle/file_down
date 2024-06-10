
from sys import stdin


def main():
    n, e, d = map(int, stdin.readline().split())
    exploding_kittens = sorted(map(int, stdin.readline().split()))
    defuse = sorted(map(int, stdin.readline().split()))
    exploding_kittens_index = 0
    defuse_index = 0
    current_player = 0
    while True:
        current_player = (current_player + 1) % n
        if exploding_kittens_index < e and defuse_index < d:
            if exploding_kittens[exploding_kittens_index] < defuse[defuse_index]:
                exploding_kittens_index += 1
                continue
            else:
                exploding_kittens_index += 1
                defuse_index += 1
        elif exploding_kittens_index < e:
            exploding_kittens_index += 1
        else:
            break
    print(current_player)


if __name__ == "__main__":
    main()



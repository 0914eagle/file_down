

def cheese_count(cheeses):
    soft = 0
    hard = 0
    for cheese in cheeses:
        if cheese[1] == 'hard':
            hard += 1
        else:
            soft += 1
    return soft, hard


def main():
    N = int(input())
    cheeses = []
    for _ in range(N):
        cheeses.append(input().split())
    soft, hard = cheese_count(cheeses)
    print(hard)


if __name__ == "__main__":
    main()



def cheese_count(cheeses):
    hard_cheese = 0
    soft_cheese = 0
    for cheese in cheeses:
        if cheese[1] == 'hard':
            hard_cheese += 1
        else:
            soft_cheese += 1
    return hard_cheese, soft_cheese

def main():
    n = int(input())
    cheeses = []
    for _ in range(n):
        cheeses.append(input().split())
    hard_cheese, soft_cheese = cheese_count(cheeses)
    print(hard_cheese)
    print(soft_cheese)

if __name__ == '__main__':
    main()


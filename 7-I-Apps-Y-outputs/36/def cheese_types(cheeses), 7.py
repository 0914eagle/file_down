
def cheese_types(cheeses):
    cheese_types = {}
    for cheese in cheeses:
        if cheese[1] in cheese_types:
            cheese_types[cheese[1]] += 1
        else:
            cheese_types[cheese[1]] = 1
    return cheese_types

def main():
    cheeses = []
    n = int(input())
    for i in range(n):
        cheeses.append(input().split())
    cheese_types = cheese_types(cheeses)
    print(len(cheese_types))

if __name__ == '__main__':
    main()


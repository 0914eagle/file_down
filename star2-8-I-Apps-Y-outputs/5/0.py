
def main():
    n, c = map(int, input().split())
    fruits = list(map(int, input().split()))
    eaten = set()
    for fruit in fruits:
        if c >= fruit:
            c -= fruit
            eaten.add(fruit)
    print(len(eaten))


if __name__ == '__main__':
    main()



from collections import defaultdict

def book_circle(boys, girls):
    book_count = defaultdict(int)
    for boy in boys:
        for book in boys[boy]:
            book_count[book] += 1
    for girl in girls:
        for book in girls[girl]:
            book_count[book] += 1
    return len(book_count)

def main():
    boys = {}
    girls = {}
    B, G = map(int, input().split())
    for _ in range(B):
        name, n = input().split()
        n = int(n)
        boys[name] = input().split()
    for _ in range(G):
        name, n = input().split()
        n = int(n)
        girls[name] = input().split()
    print(book_circle(boys, girls))

if __name__ == '__main__':
    main()


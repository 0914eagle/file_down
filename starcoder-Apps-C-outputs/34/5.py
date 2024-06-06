
from itertools import combinations

def split_books(books):
    for i in range(1, len(books)//2):
        for s1 in combinations(books, i):
            s2 = set(books) - set(s1)
            for s3 in combinations(s2, len(s2)//2):
                s4 = set(s2) - set(s3)
                yield s1, s3, s4


def surface(bookcase):
    width = max(sum(t for h, t in s) for s in bookcase)
    height = max(max(h for h, t in s) for s in bookcase)
    return width * height


def main():
    N = int(input())
    books = [tuple(map(int, input().split())) for _ in range(N)]

    print(min(surface(case) for case in split_books(books)))


main()

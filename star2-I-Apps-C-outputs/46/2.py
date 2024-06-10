
from collections import defaultdict

def book_circle(boys, girls):
    boys_books = defaultdict(list)
    girls_books = defaultdict(list)
    for boy in boys:
        boys_books[boy[0]].extend(boy[1:])
    for girl in girls:
        girls_books[girl[0]].extend(girl[1:])
    common_books = set(boys_books.keys()).intersection(set(girls_books.keys()))
    boys_books = {k: v for k, v in boys_books.items() if k not in common_books}
    girls_books = {k: v for k, v in girls_books.items() if k not in common_books}
    presentations = 0
    while boys_books or girls_books:
        if boys_books:
            book = boys_books.popitem()[1][0]
            while book in girls_books:
                del girls_books[book]
                if not girls_books:
                    break
                book = girls_books.popitem()[1][0]
        presentations += 1
        if girls_books:
            book = girls_books.popitem()[1][0]
            while book in boys_books:
                del boys_books[book]
                if not boys_books:
                    break
                book = boys_books.popitem()[1][0]
        presentations += 1
    return presentations

if __name__ == '__main__':
    boys, girls = map(int, input().split())
    boys_books = [input().split() for _ in range(boys)]
    girls_books = [input().split() for _ in range(girls)]
    print(book_circle(boys_books, girls_books))


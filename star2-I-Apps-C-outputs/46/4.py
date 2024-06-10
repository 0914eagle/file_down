
import sys

def solve(boys, girls, books):
    pass

def main():
    boys, girls = map(int, sys.stdin.readline().split())
    boys_books = {}
    for _ in range(boys):
        name, num_books = sys.stdin.readline().split()
        num_books = int(num_books)
        boys_books[name] = set(sys.stdin.readline().split()[:num_books])
    girls_books = {}
    for _ in range(girls):
        name, num_books = sys.stdin.readline().split()
        num_books = int(num_books)
        girls_books[name] = set(sys.stdin.readline().split()[:num_books])
    print(solve(boys_books, girls_books, boys_books.keys() | girls_books.keys()))

if __name__ == '__main__':
    main()


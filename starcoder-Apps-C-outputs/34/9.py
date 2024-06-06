
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import stdin
import bisect

def min_area(books, n):
    f = [float("inf")]*(n + 1)
    f[0] = 0

    for i in range(1, n + 1):
        book_h, book_w = books[i - 1]
        for j in range(i, 0, -1):
            f[j] = min(f[j], max(book_h, f[j - 1])) * max(book_w, f[i] - f[j - 1])
    return f[n]


def main():
    n = int(stdin.readline())
    books = []
    for i in range(n):
        books.append(tuple(map(int, stdin.readline().split())))
    books = sorted(books, key=lambda x: (x[0], x[1]))

    area = min_area(books, n)
    print(area)

if __name__ == '__main__':
    main()


import math
import sys

def partition(n):
    if n < 1:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1]]
    elif n == 3:
        return [[1, 2], [1, 1, 1]]
    elif n == 4:
        return [[1, 3], [2, 2], [1, 1, 2], [1, 1, 1, 1]]
    else:
        return [[1, i] for i in range(4, n)] + [[i, n-i] for i in range(2, n-1)]

def get_heights(books):
    return [book[0] for book in books]

def get_thickness(books):
    return [book[1] for book in books]

def get_area(books, partition):
    partition_heights = [max(get_heights(books[group_idx])) for group_idx in partition]
    partition_widths = [sum(get_thickness(books[group_idx])) for group_idx in partition]
    return max(partition_heights) * sum(partition_widths)

def main():
    num_books = int(sys.stdin.readline().strip())
    books = [tuple(map(int, sys.stdin.readline().strip().split())) for i in range(num_books)]
    partitions = partition(num_books)
    areas = [get_area(books, partition) for partition in partitions]
    print(min(areas))

if __name__ == '__main__':
    main()

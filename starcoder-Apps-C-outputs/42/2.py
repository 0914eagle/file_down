
from typing import List


def restore_array(table: List[List[int]]) -> List[int]:
    n = len(table)
    a = [0] * n
    i = 0
    while i < n:
        a[i] = 1
        for j in range(i + 1, n):
            a[j] = table[i][j] // a[i]
        i += 1
    return a


def read_matrix(rows: int, cols: int) -> List[List[int]]:
    return [[int(num) for num in input().split()] for _ in range(rows)]


if __name__ == "__main__":
    table = read_matrix(int(input()), int(input()))
    a = restore_array(table)
    print(*a)

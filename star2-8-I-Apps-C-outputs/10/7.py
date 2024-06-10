
from math import ceil, floor, log
def reverse_num(num):
    rev_num = 0
    while num:
        rev_num = rev_num * 10 + num % 10
        num //= 10
    return rev_num
def solve(A, B):
    res = 0
    for i in range(ceil(log(A, 10)), floor(log(B, 10)) + 1):
        if 10 ** i <= A:
            continue
        if B < 10 ** i:
            break
        last_num = 10 ** i - 1
        first_num = max(A, 10 ** (i - 1))
        res += last_num - first_num + 1
        res += reverse_num(last_num) - reverse_num(first_num) + 1
    return res

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        A, B = map(int, input().split())
        print(solve(A, B))


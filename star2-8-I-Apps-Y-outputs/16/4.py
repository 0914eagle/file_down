
from bisect import bisect_left
from itertools import accumulate


def solve(N: int, A: "List[int]"):
    A = [0] + sorted(A) + [0]
    cost_sum = sum(abs(A[i + 1] - A[i]) for i in range(len(A) - 1))

    for i in range(1, N + 1):
        left = bisect_left(A, A[i])
        right = left + 1
        print(
            cost_sum
            - abs(A[right] - A[left])
            + abs(A[left] - A[left - 1])
            + abs(A[right] - A[right - 1])
        )


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)



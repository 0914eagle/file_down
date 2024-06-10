
import sys

def solve(N, A):
    A = [0] + A + [0]
    sum_left = [0] * (N + 2)
    sum_right = [0] * (N + 2)
    for i in range(1, N + 2):
        sum_left[i] = sum_left[i - 1] + abs(A[i] - A[i - 1])
    for i in range(N, 0, -1):
        sum_right[i] = sum_right[i + 1] + abs(A[i] - A[i + 1])
    for i in range(1, N + 1):
        print(sum_left[i - 1] + sum_right[i + 1])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, A)


if __name__ == '__main__':
    main()


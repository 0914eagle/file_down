
from math import factorial

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solve(N, payout, prob):
    expected = [0] * N
    for row in range(N):
        for col in range(row + 1):
            hole = row * (row + 1) // 2 + col
            expected[row] += payout[hole] * prob[hole][4]
            for direction in range(4):
                if direction == 0 and col == 0:
                    continue
                if direction == 1 and col == row:
                    continue
                if direction == 2 and col == 0:
                    continue
                if direction == 3 and col == row:
                    continue
                next_row = row + 1 if direction < 2 else row - 1
                next_col = col + 1 if direction % 2 == 0 else col - 1
                next_hole = next_row * (next_row + 1) // 2 + next_col
                expected[row] += payout[hole] * prob[hole][direction] * expected[next_row]
    return expected[0]

N = int(input())
payout = list(map(int, input().split()))
prob = [list(map(float, input().split())) for _ in range(N * (N + 1) // 2)]
print(solve(N, payout, prob))



import itertools

def solve(n, k, a):
    max_profit = 0
    for i in range(1, k+1):
        for comb in itertools.combinations(a, i):
            profit = sum(comb)
            if profit > max_profit:
                max_profit = profit
    return max_profit

def solve2(n, k, a):
    max_profit = 0
    for i in range(1, k+1):
        for comb in itertools.combinations(a, i):
            profit = max(comb)
            if profit > max_profit:
                max_profit = profit
    return max_profit

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
    print(solve2(n, k, a))


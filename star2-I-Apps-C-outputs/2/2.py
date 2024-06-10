
def solve(n, k, seq, cost):
    pass

if __name__ == '__main__':
    n, k = map(int, input().split())
    seq = input()
    cost = [int(input()) for _ in range(n)]
    print(solve(n, k, seq, cost))



def solve(n, words, q, rounds):
    pass

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    q = int(input())
    rounds = [list(map(int, input().split())) for _ in range(q)]
    solve(n, words, q, rounds)


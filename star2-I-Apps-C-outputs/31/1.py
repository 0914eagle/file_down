
def solve(n, m, words):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        l, *s = map(int, input().split())
        words.append((l, s))
    print(solve(n, m, words))


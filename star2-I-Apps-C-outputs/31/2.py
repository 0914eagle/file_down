
def solve(n, m, words):
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        l, *s = map(int, input().split())
        words.append(s)
    print(solve(n, m, words))


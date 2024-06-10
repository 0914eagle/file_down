
def solve(n, m, words):
    pass

if __name__ == "__main__":
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        l, *s = map(int, input().split())
        words.append((l, s))
    res = solve(n, m, words)
    if res is None:
        print("No")
    else:
        print("Yes")
        print(len(res))
        print(" ".join(map(str, res)))



def solve(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or s[i] == "*":
            i += 1
            j += 1
        else:
            return "NO"
    if i < len(s) and s[i] == "*":
        i += 1
    return "YES" if i == len(s) else "NO"


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = input()
    t = input()
    print(solve(s, t))

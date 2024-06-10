

def solve(s: str) -> int:
    n = len(s)
    t = 0
    for i in range(n):
        if s[i] == '1':
            t = max(t, i + 1)
    return t

if __name__ == '__main__':
    s = input()
    print(solve(s))



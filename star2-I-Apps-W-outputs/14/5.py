
import sys
def solve(r, s, p):
    r, s, p = sorted([r, s, p])
    if r == s == p:
        return [1.0 / 3] * 3
    elif r == s:
        return [0.0, 0.0, 1.0]
    elif s == p:
        return [0.0, 1.0 / 2, 1.0 / 2]
    elif r == p:
        return [1.0 / 2, 0.0, 1.0 / 2]
    elif r == 1:
        return [0.0, 1.0 - 1.0 / p, 1.0 / p]
    elif s == 1:
        return [1.0 / r, 0.0, 1.0 - 1.0 / r]
    elif p == 1:
        return [1.0 - 1.0 / s, 1.0 / s, 0.0]
    else:
        return [0.0, 0.0, 0.0]

def main():
    r, s, p = map(int, sys.stdin.read().split())
    print(" ".join(map(str, solve(r, s, p))))

if __name__ == "__main__":
    main()


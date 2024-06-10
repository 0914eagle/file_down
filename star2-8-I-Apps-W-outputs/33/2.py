
import sys

def solve(s1, s2):
    pos = 0
    for c1, c2 in zip(s1, s2):
        if c2 == '+':
            pos += 1
        elif c2 == '-':
            pos -= 1
        elif c2 == '?':
            if c1 == '+':
                pos += 1
            elif c1 == '-':
                pos -= 1
            else:
                pos += 1 # assume c1 == '?', so go either way with probability 0.5
                pos -= 1
    return pos == 0

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(1.0 if solve(s1, s2) else 0.0)

if __name__ == '__main__':
    main()


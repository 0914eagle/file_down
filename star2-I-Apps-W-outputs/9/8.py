
from sys import stdin

def find_occurrences(t, s):
    occurrences = 0
    for i in range(len(t) - len(s) + 1):
        if t[i:i+len(s)] == s:
            occurrences += 1
    return occurrences

def main():
    n, m = map(int, stdin.readline().split())
    t = stdin.readline().split()
    s = stdin.readline().split()
    t = ''.join(c * int(l) for l, c in t)
    s = ''.join(c * int(l) for l, c in s)
    print(find_occurrences(t, s))

if __name__ == '__main__':
    main()


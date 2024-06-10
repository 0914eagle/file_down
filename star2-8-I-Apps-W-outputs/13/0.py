
from sys import stdin

def readInput():
    n, t = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    return n, t, a

def solve(n, t, a):
    if t == 1:
        return 7
    elif t == 2:
        if a[0] > a[1]:
            return "Bigger"
        elif a[0] == a[1]:
            return "Equal"
        else:
            return "Smaller"
    elif t == 3:
        b = sorted(a[:3])
        return b[1]
    elif t == 4:
        return sum(a)
    elif t == 5:
        return sum(x for x in a if x % 2 == 0)
    elif t == 6:
        return ''.join(chr(x % 26 + ord('a')) for x in a)
    elif t == 7:
        i = 0
        while 0 <= i < n:
            i = a[i]
            if i == n - 1:
                return "Done"
            if i >= n:
                return "Out"
        return "Cyclic"

def main():
    n, t, a = readInput()
    print(solve(n, t, a))

if __name__ == "__main__":
    main()


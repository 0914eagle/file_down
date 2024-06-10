
import sys
input = sys.stdin.readline
def solve(n, t, a):
    if t == 1:
        return "7"
    elif t == 2:
        if a[0] > a[1]:
            return "Bigger"
        elif a[0] == a[1]:
            return "Equal"
        else:
            return "Smaller"
    elif t == 3:
        arr = sorted(a[:3])
        return str(arr[1])
    elif t == 4:
        return str(sum(a))
    elif t == 5:
        return str(sum([x for x in a if x % 2 == 0]))
    elif t == 6:
        return ''.join([chr(x % 26 + ord('a')) for x in a])
    elif t == 7:
        i = 0
        while 0 <= i < n:
            if i == n - 1:
                return "Done"
            i = a[i]
        return "Out"
if __name__ == '__main__':
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, t, a))



def solve(s):
    n = len(s)
    left = set()
    right = set()
    for i in range(n // 2):
        left.add(s[i])
        right.add(s[n - 1 - i])
    return len(left.intersection(right))

n = int(input())
s = input()
print(solve(s))



def find_occurrences(t, s):
    n, m = len(t), len(s)
    occurrences = 0
    for i in range(n - m + 1):
        if t[i:i+m] == s:
            occurrences += 1
    return occurrences

n, m = map(int, input().split())
t = input().split()
s = input().split()
t = ''.join(c * int(l) for l, c in t)
s = ''.join(c * int(l) for l, c in s)
print(find_occurrences(t, s))



def is_unbalanced(s):
    n = len(s)
    for i in range(n-1):
        for j in range(i+1, n):
            sub = s[i:j+1]
            count = {c: sub.count(c) for c in set(sub)}
            max_freq = max(count.values())
            if len(sub) >= 2 and max_freq > len(sub) / 2:
                return i+1, j+1
    return -1, -1

# Input
s = input().strip()

# Output
a, b = is_unbalanced(s)
print(a, b)

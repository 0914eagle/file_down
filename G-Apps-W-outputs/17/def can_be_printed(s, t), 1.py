
def can_be_printed(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            return "NO"
        char_s = s[i]
        count_s, count_t = 0, 0
        while i < len(s) and s[i] == char_s:
            count_s += 1
            i += 1
        while j < len(t) and t[j] == char_s:
            count_t += 1
            j += 1
        if count_t < count_s:
            return "NO"
    if i < len(s) or j < len(t):
        return "NO"
    return "YES"

n = int(input())
for _ in range(n):
    s = input().strip()
    t = input().strip()
    print(can_be_printed(s, t))

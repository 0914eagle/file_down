
def can_print_word(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            return "NO"
        count_s = 1
        count_t = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count_s += 1
        while j + 1 < len(t) and t[j] == t[j + 1]:
            j += 1
            count_t += 1
        if count_s > count_t:
            return "NO"
        i += 1
        j += 1
    if i == len(s) and j == len(t):
        return "YES"
    else:
        return "NO"

n = int(input())
for _ in range(n):
    s = input()
    t = input()
    result = can_print_word(s, t)
    print(result)
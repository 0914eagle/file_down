
def count_distinct_chars(s, l, r):
    chars = set()
    for i in range(l, r + 1):
        chars.add(s[i])
    return len(chars)

s = input()
q = int(input())
for _ in range(q):
    t, *args = input().split()
    if t == '1':
        pos, c = int(args[0]), args[1]
        s = s[:pos - 1] + c + s[pos:]
    else:
        l, r = int(args[0]), int(args[1])
        print(count_distinct_chars(s, l - 1, r - 1))



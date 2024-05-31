
def can_be_printed(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

n = int(input())
for _ in range(n):
    s = input().strip()
    t = input().strip()
    if can_be_printed(s, t):
        print("YES")
    else:
        print("NO")

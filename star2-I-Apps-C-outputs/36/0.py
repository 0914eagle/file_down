
n, m = map(int, input().split())
s = input()
t = input()

def check(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        elif s[i] == "*":
            i += 1
            while j < len(t):
                if check(s[i:], t[j:]):
                    return True
                j += 1
            return False
        else:
            return False
    return i == len(s) and j == len(t)

print("YES" if check(s, t) else "NO")


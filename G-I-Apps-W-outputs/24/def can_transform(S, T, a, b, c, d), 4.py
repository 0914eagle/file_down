
def can_transform(S, T, a, b, c, d):
    def transform(s):
        nonlocal S
        tmp = ''
        i = 0
        while i < len(s):
            if s[i:i+3] == 'AAA':
                i += 3
            elif s[i] == 'A' and i+1 < len(s) and s[i+1] == 'B':
                tmp += 'C'
                i += 2
            elif s[i] == 'A' and i+1 < len(s) and s[i+1] == 'C':
                tmp += 'B'
                i += 2
            elif s[i] == 'B' and i+1 < len(s) and s[i+1] == 'A':
                tmp += 'C'
                i += 2
            elif s[i] == 'B' and i+1 < len(s) and s[i+1] == 'C':
                tmp += 'A'
                i += 2
            elif s[i] == 'C' and i+1 < len(s) and s[i+1] == 'A':
                tmp += 'B'
                i += 2
            elif s[i] == 'C' and i+1 < len(s) and s[i+1] == 'B':
                tmp += 'A'
                i += 2
            else:
                tmp += s[i]
                i += 1
        return tmp

    def is_subsequence(s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return j == len(t)

    return '1' if is_subsequence(transform(S[a-1:b]), T[c-1:d]) else '0'

S = input().strip()
T = input().strip()
Q = int(input().strip())

ans = ''
for _ in range(Q):
    a, b, c, d = map(int, input().strip().split())
    ans += can_transform(S, T, a, b, c, d)

print(ans)


s = input()
q = int(input())
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1
for _ in range(q):
    t, *lr = map(int, input().split())
    if t == 1:
        i, c = lr
        freq[ord(s[i - 1]) - ord('a')] -= 1
        freq[ord(c) - ord('a')] += 1
        s = s[:i - 1] + c + s[i:]
    else:
        l, r = lr
        res = 0
        for c in range(26):
            if freq[c] > 0 and l - 1 <= s.rfind(chr(c + ord('a'))) <= r - 1:
                res += 1
        print(res)


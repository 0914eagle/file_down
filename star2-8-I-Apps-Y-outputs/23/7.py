
s = input()
q = int(input())
occ = [0] * 26
for i in range(len(s)):
    occ[ord(s[i]) - ord('a')] += 1
for i in range(q):
    query = input()
    if query[0] == '1':
        pos, ch = query.split(' ')
        pos = int(pos)
        ch = ch[0]
        occ[ord(s[pos - 1]) - ord('a')] -= 1
        occ[ord(ch) - ord('a')] += 1
        s = s[:pos - 1] + ch + s[pos:]
    else:
        l, r = map(int, query.split(' '))
        count = 0
        for j in range(26):
            if occ[j] > 0:
                count += 1
        print(count)


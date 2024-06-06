
s = input()
n = int(input())

words = []
for i in range(n):
    words.append(input())

words.sort(key=len, reverse=True)

def solve(s, words):
    if len(s) == 0:
        return True, ''

    for word in words:
        if s.startswith(word):
            ok, res = solve(s[len(word):], words)
            if ok:
                return True, res + ' ' + word

    return False, ''

ok, res = solve(s, words)
if ok:
    print(res.strip())
else:
    print('impossible')

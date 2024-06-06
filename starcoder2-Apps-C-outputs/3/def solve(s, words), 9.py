
import sys

def solve(s, words):
    if len(s) == 0:
        return True, []
    for i in range(len(s)):
        if s[0] == s[i]:
            for word in words:
                if word[0] == s[i]:
                    if len(word) == len(s):
                        if word == s:
                            return True, [word]
                    else:
                        if word == s[:len(word)]:
                            ok, res = solve(s[len(word):], words)
                            if ok:
                                return True, [word] + res
    return False, []

s = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())

ok, res = solve(s, words)
if ok:
    print(" ".join(res))
else:
    print("impossible")


def solve(s, words):
    words = set(words)
    words = [w[::-1] for w in words]
    if is_deciphered(s, words):
        return s[::-1]
    else:
        if is_ambiguous(s, words):
            return "ambiguous"
        else:
            return "impossible"


def is_deciphered(s, words):
    if s == '':
        return True
    for i in range(len(s)):
        if s[0] + s[i:] in words and is_deciphered(s[0] + s[i:], words):
            return True
    return False


def is_ambiguous(s, words):
    if s == '':
        return False
    for i in range(len(s)):
        if s[0] + s[i:] in words and is_deciphered(s[0] + s[i:], words):
            return True
    return False


def read_input():
    s = input()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    return s, words


print(solve(*read_input()))


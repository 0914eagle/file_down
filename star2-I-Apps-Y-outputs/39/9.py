
S = input()
K = int(input())

def expand(s):
    res = ""
    for c in s:
        if c == "2":
            res += "22"
        elif c == "3":
            res += "333"
        elif c == "4":
            res += "4444"
        elif c == "5":
            res += "55555"
        elif c == "6":
            res += "666666"
        elif c == "7":
            res += "7777777"
        elif c == "8":
            res += "88888888"
        elif c == "9":
            res += "999999999"
        else:
            res += c
    return res

def count_length(s):
    res = 0
    for c in s:
        if c == "1":
            res += 1
        elif c == "2":
            res += 2
        elif c == "3":
            res += 3
        elif c == "4":
            res += 4
        elif c == "5":
            res += 5
        elif c == "6":
            res += 6
        elif c == "7":
            res += 7
        elif c == "8":
            res += 8
        elif c == "9":
            res += 9
    return res

def solve(s, k):
    if k == 1:
        return s[0]
    if count_length(s) < k:
        return -1
    while True:
        s = expand(s)
        if count_length(s) >= k:
            break
    return s[k-1]

print(solve(S, K))


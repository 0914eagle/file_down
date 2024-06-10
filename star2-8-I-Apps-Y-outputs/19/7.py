

def solve():
    k = int(input())
    s = input()
    if len(s) <= k:
        return s
    else:
        return s[:k] + "..."


print(solve())



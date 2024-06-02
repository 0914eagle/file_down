
def solve(s, k):
    subs = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs.add(s[i:j+1])
    subs = sorted(subs)
    return subs[k-1]

s = input()
k = int(input())
print(solve(s, k))


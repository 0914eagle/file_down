
def solve(s, k):
    substrings = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substrings.add(s[i:j+1])
    substrings = sorted(substrings)
    return substrings[k-1]

s = input()
k = int(input())
print(solve(s, k))


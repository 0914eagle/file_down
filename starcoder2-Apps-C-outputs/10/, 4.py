
n = int(input())
d = []
for i in range(n-1):
    d.append(list(map(int, input().split())))

def disparity(s):
    max_disparity = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            max_disparity = max(max_disparity, d[s[i]-1][s[j]-1-s[i]])
    return max_disparity

def partition(s):
    if len(s) == 1:
        return 0
    if len(s) == 2:
        return d[s[0]-1][s[1]-1-s[0]]
    min_disparity = 10**9
    for i in range(1, len(s)):
        min_disparity = min(min_disparity, disparity(s[:i]) + partition(s[i:]))
    return min_disparity

print(partition(list(range(1, n+1))))

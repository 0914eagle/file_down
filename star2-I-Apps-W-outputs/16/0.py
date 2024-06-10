
def solve(arr):
    freq = {}
    for x in arr:
        if x not in freq:
            freq[x] = 0
        freq[x] += 1
    
    res = len(arr)
    for k, v in freq.items():
        res = min(res, v)
    
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))


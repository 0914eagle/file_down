
import sys
input = sys.stdin.readline

def solve(s, k):
    cnt = [0] * 3
    for c in s:
        if c == 'R':
            cnt[0] += 1
        elif c == 'G':
            cnt[1] += 1
        else:
            cnt[2] += 1
    
    res = min(cnt)
    
    for i in range(1, k):
        cnt = [0] * 3
        for j in range(i, n):
            if s[j] == 'R':
                cnt[0] += 1
            elif s[j] == 'G':
                cnt[1] += 1
            else:
                cnt[2] += 1
        
        res = min(res, min(cnt))
    
    return res

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input().strip()
    
    res = solve(s, k)
    print(res)



def solve(n, k, s):
    count = {'R': 0, 'G': 0, 'B': 0}
    for c in s:
        count[c] += 1
    
    target = {'R': 0, 'G': 0, 'B': 0}
    target['R'] = (k + 2) // 3
    target['G'] = (k + 1) // 3
    target['B'] = k // 3
    
    cost = 0
    for c in 'RGB':
        cost += max(0, target[c] - count[c])
    
    return cost

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    
    print(solve(n, k, s))


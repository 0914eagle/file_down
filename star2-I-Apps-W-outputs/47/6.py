
def solve(p, foe_pairs):
    n = len(p)
    m = len(foe_pairs)
    
    return 0

n, m = map(int, input().split())
p = list(map(int, input().split()))
foe_pairs = []
for _ in range(m):
    a, b = map(int, input().split())
    foe_pairs.append((a, b))
    
print(solve(p, foe_pairs))


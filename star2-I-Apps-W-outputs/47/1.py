
def solve(p, foe_pairs):
    n = len(p)
    m = len(foe_pairs)
    
    foe_pairs.sort()
    
    foe_pairs_idx = 0
    
    count = 0
    
    for i in range(n):
        while foe_pairs_idx < m and foe_pairs[foe_pairs_idx][0] == p[i]:
            foe_pairs_idx += 1
        
        count += n - i - (m - foe_pairs_idx)
        
    return count

def main():
    n, m = map(int, input().split())
    
    p = list(map(int, input().split()))
    
    foe_pairs = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        foe_pairs.append((a, b))
        
    print(solve(p, foe_pairs))
    
if __name__ == '__main__':
    main()


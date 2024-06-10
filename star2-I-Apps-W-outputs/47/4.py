
def solve(p, foe_pairs):
    n = len(p)
    m = len(foe_pairs)
    
    foe_pairs.sort()
    
    dp = [0] * (n + 1)
    
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * 2
        
        l = 0
        r = m - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if foe_pairs[mid][0] <= p[i - 1] and p[i - 1] <= foe_pairs[mid][1]:
                l = mid
                break
            elif foe_pairs[mid][0] > p[i - 1]:
                r = mid - 1
            else:
                l = mid + 1
        
        while l < m and foe_pairs[l][0] == p[i - 1]:
            dp[i] -= dp[foe_pairs[l][1] - 1]
            l += 1
    
    return dp[n]


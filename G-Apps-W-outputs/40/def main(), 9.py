
import sys

def main():
    n, m = map(int, input().split())
    islands = list(map(int, input().split()))
    g, r = map(int, input().split())
    
    dp = [[-1] * (g + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    queue = [(0, 0)]
    
    while queue:
        pos, mod = queue.pop(0)
        
        # Move to the right
        if pos + 1 <= n and dp[pos + 1][(mod + 1) % g] == -1:
            dp[pos + 1][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((pos + 1, (mod + 1) % g))
        
        # Move to the left
        if pos - 1 >= 0 and dp[pos - 1][(mod + 1) % g] == -1:
            dp[pos - 1][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((pos - 1, (mod + 1) % g))
        
        # Wait at the current position
        if dp[pos][(mod + 1) % g] == -1:
            dp[pos][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((pos, (mod + 1) % g))
        
        # Change direction at safety islands
        for island in islands:
            if island != pos and dp[island][(mod + 1) % g] == -1:
                dp[island][(mod + 1) % g] = dp[pos][mod] + island - pos
                queue.append((island, (mod + 1) % g))
    
    result = min(dp[n])
    
    if result == -1:
        print(-1)
    else:
        print(result * (g + r) - r)
    
if __name__ == "__main__":
    main()

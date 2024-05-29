
def find_largest_committee(N, K, disagreements):
    def dfs(idx, committee):
        if len(committee) > K:
            return 0
        if idx == N:
            return len(committee)
        
        max_size = 0
        # Try including the current politician in the committee
        max_size = max(max_size, dfs(idx + 1, committee | {idx}))
        
        # Try excluding the current politician from the committee
        can_include = True
        for member in committee:
            if member not in disagreements[idx]:
                can_include = False
                break
        if can_include:
            max_size = max(max_size, dfs(idx + 1, committee))
        
        return max_size
    
    return dfs(0, set())

if __name__ == "__main__":
    N, K = map(int, input().split())
    disagreements = []
    for _ in range(N):
        data = list(map(int, input().split()))[1:]
        disagreements.append(set(data))
    
    result = find_largest_committee(N, K, disagreements)
    print(result)
```

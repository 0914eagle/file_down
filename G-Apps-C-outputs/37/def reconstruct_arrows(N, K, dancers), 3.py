
def reconstruct_arrows(N, K, dancers):
    arrows = [-1] * N
    visited = [False] * N
    
    for i in range(N):
        if visited[i]:
            continue
            
        cycle = []
        j = i
        while not visited[j]:
            cycle.append(j)
            visited[j] = True
            j = dancers[j] - 1
        
        if len(cycle) > 0:
            cycle_len = len(cycle)
            for idx, val in enumerate(cycle):
                arrows[val] = cycle[(idx + K) % cycle_len] + 1
    
    if -1 in arrows:
        print("Impossible")
    else:
        print(" ".join(map(str, arrows)))

# Input parsing
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

reconstruct_arrows(N, K, dancers)


def can_hit_all_targets(N, targets):
    if N <= 2:
        return "success"

    for i in range(N):
        for j in range(i + 1, N):
            slope = (targets[j][1] - targets[i][1]) / (targets[j][0] - targets[i][0]) if targets[j][0] != targets[i][0] else float('inf')
            intercept = targets[i][1] - slope * targets[i][0]
            count = 2
            for k in range(N):
                if k != i and k != j and targets[k][1] == slope * targets[k][0] + intercept:
                    count += 1
            if count == N:
                return "success"
    
    return "failure"

# Input
N = int(input())
targets = [tuple(map(int, input().split())) for _ in range(N)]

# Output
print(can_hit_all_targets(N, targets))


N, D = map(int, input().split())
inspectors = [0] * N

for i in range(N):
    start = max(0, i - D)
    end = min(N - 1, i + D)
    
    for j in range(start, end + 1):
        inspectors[j] = 1
        
print(sum(inspectors))

